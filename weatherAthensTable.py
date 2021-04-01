import requests

import json

from tabulate import tabulate
     
def jprint(obj):

    text = json.dumps(obj, sort_keys=True, indent=4)

    return text

def jload(obj):

    loaded_json = json.loads(formatted_json)

    return loaded_json


def get_weather_json():

    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Athens&appid=13ad4f635eb2009d5356b77ac5442f94")

    if (response.status_code == 200):

        return response.json()

    else :

        print ("Unsuccessful Request with error code :",response.status_code)

        return None

weather_json = get_weather_json()

formatted_json = jprint(weather_json)

loaded_json = jload(weather_json)

# Add the headers of the table as an array item on the list

temperature_values_list = [['Temperaure','Temperature Feeling','Max Temperature','Min Temperature', 'Humidity']]

temperature_values_array = []

# Temperature

temperature_main = round(loaded_json['main']['temp'] - 274.15,2)

temperature_values_array.append(str(temperature_main) + ' °C')

# Temperature Feel

temperature_feel = round(loaded_json['main']['feels_like'] - 274.15,2)

temperature_values_array.append(str(temperature_feel) + ' °C')

# Max Temperature

temperature_max = round(loaded_json['main']['temp_max'] - 274.15,2)

temperature_values_array.append(str(temperature_max) + ' °C')

# Min Temperature

temperature_min = round(loaded_json['main']['temp_min'] - 274.15,2)

temperature_values_array.append(str(temperature_min) + ' °C')

# Humidity

humidity_main = round(loaded_json['main']['humidity'])

temperature_values_array.append(str(humidity_main) + ' %')

# Add the other meteo values of the table as an array item on the list

temperature_values_list.append(temperature_values_array)

print(tabulate(temperature_values_list))
