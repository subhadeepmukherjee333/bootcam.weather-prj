
import requests
# import os
from datetime import datetime

api_key = '3793ecc2cc31376bf4dbea807cdc2797'
location = input("Enter the city name: ")

api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + api_key
api_link = requests.get(api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
humidity = api_data['main']['humidity']
wind_speed = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("**************************************************************")
print("Weather Status for - {}  // {}".format(location.upper(), date_time))
print("**************************************************************")

print("Current temperature is: {:.2f} deg C".format(temp_city))
print("Current weather desc  :", weather_desc)
print("Current Humidity      :", humidity, '%')
print("Current wind speed    :", wind_speed, 'kmph')



with open('weather.txt', 'w') as f:
      f.write("**************************************************************")
      f.write("\nWeather Status for - {}  // {}".format(location.upper(), date_time))
      f.write("\n**************************************************************")
      f.write("\nCurrent temperature is: {:.2f} deg C".format(temp_city))
      f.write("\nCurrent weather desc  :" + weather_desc)
      f.write("\nCurrent Humidity      :" + str(humidity) + '%')
      f.write("\nCurrent wind speed    :" + str(wind_speed) + 'kmph')