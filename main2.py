# fish
# virtualenv venv
# source venv/bin/activate.fish
# pip install requests
# pip install python-dotenv
# pip freeze > requirements.txt
# Переключить интерпритатор

# d5bb44d0fa8e39e2339c9019d833d826
import requests
from datetime import datetime
from os import getenv, system
from dotenv import load_dotenv
load_dotenv()

WEATHER_API = getenv('WEATHER_API')
def WetherService(get_city, API=WEATHER_API):
    """
    Ваш бот-метеоролог мгновенно показывает погоду в любом городе, 
    предоставляя актуальную информацию о температуре воздуха, влажности и вероятности дождя. 
    Это помогает планировать дела эффективнее и быть в курсе 
    погодных событий в режиме реального времени
    get_city = 'Almaty'
    api = WEATHER_API

    WeatherService(get_city:str, API: StrApiKey) -> str
    """
    API = "4d91b754b37c6feff92c3bcbdeede521"

    url = f'https://api.openweathermap.org/data/2.5/weather?q={get_city}&appid={API}&units=metric'

    response = requests.get(url)
    data = response.json()

    informations = f"""Погода - Dk
    Название страны: {data["sys"]['country']}
    Название города: {data['name']} - {data['wether'][0]['description']}{data['clouds']['all']}%
    Температура: {data['main']['temp']}C
    Ощущается: {data['main']['feels_like']}C
    Влажност: {data['main']['humidity']}%
    Давление воздуха: {data['main']['pressure']}гПа1
    Скорость ветра: {data['wind']['speed']}м/с
    Направление ветра: {data['wind']['deg']}°
    Восход солнца: {datetime.fromtimestamp(data['sys']['sunrise'])}
    Продол-ть дня: 
    Закат солнца: {datetime.fromtimestamp(data['sys']['sunset'])}
    """

    system("clear")
    return informations
#pprint(data)

city = input("Введите газвание города: ")
print(WetherService(city))
