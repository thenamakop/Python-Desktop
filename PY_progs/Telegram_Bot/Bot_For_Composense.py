import serial
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Telegram Bot Token (Get from BotFather)
TOKEN = "8093936065:AAHhhga_xhySbj71I6El6wBJrejvVvN5gOs"

# Serial port configuration
SERIAL_PORT = 'COM3'  # Update with your port
BAUD_RATE = 9600

# Initialize serial connection
try:
    arduino = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2)
except serial.SerialException as e:
    logging.error(f"Error connecting to Arduino: {e}")
    exit(1)

def start(update: Update, context: CallbackContext) -> None:
    """Send welcome message"""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr"Hi {user.mention_markdown_v2()}\! I'm your DHT11 Sensor Bot\. "
        fr"Send /dht11 to get current temperature and humidity readings"
    )

def get_sensor_data():
    """Read sensor data from Arduino"""
    try:
        arduino.flushInput()
        arduino.write(b'R')  # Send request signal to Arduino
        data = arduino.readline().decode('utf-8').strip()
        return data
    except serial.SerialException as e:
        logging.error(f"Serial communication error: {e}")
        return None

def parse_dht_data(raw_data):
    """Parse DHT11 sensor data"""
    if "Error" in raw_data:
        return "Sensor read error - please try again"
    
    try:
        # Expected format: "Temperature:25.00C,Humidity:30.00%"
        parts = raw_data.split(',')
        temp = parts[0].split(':')[1]
        hum = parts[1].split(':')[1]
        return temp, hum
    except Exception as e:
        logging.error(f"Parsing error: {e}")
        return None, None

def dht11_command(update: Update, context: CallbackContext) -> None:
    """Handle /dht11 command"""
    raw_data = get_sensor_data()
    
    if not raw_data:
        update.message.reply_text("⚠️ Failed to communicate with Arduino")
        return
    
    if "Error" in raw_data:
        update.message.reply_text("❌ Error reading sensor. Please try again.")
        return
    
    temp, hum = parse_dht_data(raw_data)
    
    if temp and hum:
        response = (
            f"🌡 Temperature: {temp}\n"
            f"💧 Humidity: {hum}\n"
            f"------------------------\n"
            f"(DHT11 Sensor Data)"
        )
        update.message.reply_text(response)
    else:
        update.message.reply_text("⚠️ Invalid sensor data received")

def main() -> None:
    """Start the bot"""
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("dht11", dht11_command))

    # Start the bot
    updater.start_polling()
    logging.info("Bot started. Press Ctrl+C to stop.")
    
    # Run until interrupted
    updater.idle()
    
    # Cleanup
    arduino.close()
    logging.info("Serial connection closed")

if __name__ == '__main__':
    main()