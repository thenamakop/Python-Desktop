import telegram.ext
import serial
import time

# Telegram bot token (replace with your bot's token)
TOKEN = "8093936065:AAHhhga_xhySbj71I6El6wBJrejvVvN5gOs"

# Serial port for Arduino (replace with your Arduino's serial port, e.g., "/dev/ttyUSB0" for Linux, "COM3" for Windows)
SERIAL_PORT = "COM5"

# Initialize serial connection
ser = serial.Serial(SERIAL_PORT, 9600, timeout=1)
time.sleep(2)  # Wait for the serial connection to initialize


def sensors(update, context):
    try:
        # Send request to Arduino
        ser.write(b"R")

        # Read response from Arduino
        response = ser.readline().decode("utf-8").strip()

        # Parse response
        if "Failed" in response:
            message = "Failed to read from DHT11 sensor"
        else:
            temperature, humidity = map(float, response.split(","))
            message = f"Temperature: {temperature} °C\nHumidity: {humidity} %"
    except Exception as e:
        message = f"Error: {str(e)}"

    # Send message back to user
    update.message.reply_text(message)


def main():
    updater = telegram.ext.Updater()
    dp = updater.dispatcher

    # Add handler for /sensors command
    dp.add_handler(telegram.ext.CommandHandler("sensors", sensors))

    # Start the bot
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
