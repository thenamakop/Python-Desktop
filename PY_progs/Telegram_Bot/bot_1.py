import logging

import serial
import serial.tools.list_ports
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def find_arduino_port():
    """Find the port where Arduino is connected."""
    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        if "Arduino" in port.description:
            return port.device
    return None


# Initialize serial connection
arduino_port = find_arduino_port()
if arduino_port:
    ser = serial.Serial(arduino_port, 9600, timeout=1)
else:
    logger.error("Arduino not found!")
    exit(1)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text(
        "Hi! I am your DHT11 sensor bot. Use /temp to get temperature and humidity readings."
    )


async def get_sensor_data(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Get temperature and humidity data from Arduino."""
    try:
        # Clear any existing data in the buffer
        ser.reset_input_buffer()

        # Read the latest data
        data = ser.readline().decode("utf-8").strip()

        if data.startswith("TEMP:") and "HUM:" in data:
            # Parse the data
            temp_str = data.split("HUM:")[0].replace("TEMP:", "")
            hum_str = data.split("HUM:")[1]

            temperature = float(temp_str)
            humidity = float(hum_str)

            message = f"Temperature: {temperature:.1f}°C\nHumidity: {humidity:.1f}%"
        else:
            message = "Failed to get reading. Try again!"

        await update.message.reply_text(message)
    except Exception as e:
        logger.error(f"Error reading sensor: {e}")
        await update.message.reply_text(
            "Error reading sensor data. Please try again later."
        )


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token
    application = Application.builder().token("YOUR_BOT_TOKEN").build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("temp", get_sensor_data))

    # Start the Bot
    application.run_polling()


if __name__ == "__main__":
    main()
