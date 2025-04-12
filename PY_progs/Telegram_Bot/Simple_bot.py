import telebot
import requests

bot = telebot.TeleBot("7284275048:AAHlYbrvdtG73g3HVeP2IIrLFz1v2ULaeXA")
weather_api_key = "c3bb3cdd8f6010773b28deda7e76f68d"


@bot.message_handler(commands=["weather"])
def send_weather(message):
    parts = message.text.split()
    if len(parts) > 1:
        city = " ".join(parts[1:])
    else:
        city = "New York"  # Default city, change as needed
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        bot.reply_to(
            message,
            f"The weather in {city} is {weather} with a temperature of {temperature}°C.",
        )
    else:
        bot.reply_to(message, f"Sorry, I couldn't find weather information for {city}.")


bot.infinity_polling()
