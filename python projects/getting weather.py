import requests
from pprint import pprint
API_key = 'd53a1308a87d71ad5095408ca4de72ad'

city = input("Enter a city:")
base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"


weather_data = requests.get(base_url).json()
pprint(weather_data)