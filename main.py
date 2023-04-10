# virtualenv venv 
# source venv/bin/activate.fish 
# pip install requests
# pip intsall python-dotenv 
# pip freeze > requirements.txt
# Переключить итнтерпритатор

import requests
from dotenv import load_dotenv
from os import getenv
load_dotenv()

WEATHER_API = getenv('WEATHER_API')

#city = input("Введите название города: ")
city = "Almaty"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API}&units=metric"

WEATHER_API = "d5bb44d0fa8e39e2339c9019d833d826"

response = requests.get(url)
data = response.json()

print(data)

#p = getenv("PASSWORD")
#abc = getenv("name1")
#print(p)

