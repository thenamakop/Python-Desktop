import logging
import serial
import time
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Configure logging to see any potential errors or debug info.
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# --- Serial communication setup ---
# Update the SERIAL_PORT according to your system.
# Example:
#   - Windows: 'COM3'
#   - Linux: '/dev/ttyACM0' or '/dev/ttyUSB0'
SERIAL_PORT = '/dev/ttyACM0'
BAUD_RATE = 9600

# Initialize a serial connection.
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    # Give the connection a moment to settle
    time.sleep(2)
    logger.info("Serial connection established on port %s", SERIAL_PORT)
except Exception as e:
    logger.error("Failed to connect to Arduino: %s", e)
    ser = None

def get_sensor_data() -> str:
    """
    Reads a line from the serial port where Arduino sends sensor data.
    This function assumes that the Arduino sends a properly formatted string that contains 
    the sensor (DHT11) readings.
    
    If the Arduino expects a request command to send data, you can write:
        ser.write(b'R')  # for example, sending letter R to request data
    and then wait for a response.
    """
    if ser is None:
        return "Error: Serial connection not available."

    try:
        # Flush any previous lingering input data
        ser.reset_input_buffer()
        
        # In case the Arduino doesn't send data continuously, you might send a request.
        # Uncomment the following line if your Arduino expects a command.
        # ser.write(b'R')  # Request sensor reading

        # Read a line from the Arduino
        line = ser.readline().decode('utf-8').strip()
        if line:
            return line
        else:
            return "No sensor data received."
    except Exception as e:
        logger.error("Error reading from serial: %s", e)
        return f"Error reading sensor data: {e}"

def sensor_command(update: Update, context: CallbackContext) -> None:
    """
    Telegram command handler for the /sensor command.
    When a user sends the /sensor command, this function calls get_sensor_data() to fetch the data 
    and replies with the sensor value.
    """
    data = get_sensor_data()
    update.message.reply_text(f"Sensor Data: {data}")

def start(update: Update, context: CallbackContext) -> None:
    """
    A simple start command to welcome the user.
    """
    update.message.reply_text("Welcome! Send /sensor to get the latest DHT11 sensor reading.")

def main() -> None:
    # Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual Telegram bot token.
    TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
    
    # Create the Updater and pass it your bot's token.
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Register commands with the dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("sensor", sensor_command))

    # Start the bot in polling mode.
    updater.start_polling()
    logger.info("Telegram bot started. Waiting for commands...")

    # Run the bot until interrupted.
    updater.idle()

if __name__ == '__main__':
    main()
