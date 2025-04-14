import telebot
import requests

bot = telebot.TeleBot("8093936065:AAHhhga_xhySbj71I6El6wBJrejvVvN5gOs")
weather_api_key = "c3bb3cdd8f6010773b28deda7e76f68d"


@bot.message_handler(commands=["temps"])
def send_weather(message):
    parts = message.text.split()
    if len(parts) > 1:
        city = " ".join(parts[1:])
    else:
        city = "Quito"  # Default city, change as needed
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        bot.reply_to(
            message,
            f"The temperature of pile is {temperature}°C.",
        )
    else:
        bot.reply_to(message, f"Sorry, Connection Error")


bot.infinity_polling()
