import requests
import json

def jprint(obj):

    text = json.dumps(obj, sort_keys=True, indent=4)

    return text

def jload(obj):

    loaded_json = json.loads(formatted_json)

    return loaded_json


def get_weather_json():

    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Athens&appid=13ad4f635eb2009d5356b77ac5442f94")

    if (response.status_code == 200):

        print ("Successful Request")

        return response.json()

    else :

        print ("Unsuccessful Request with error code :",response.status_code)

        return None

weather_json = get_weather_json()

formatted_json = jprint(weather_json)

loaded_json = jload(weather_json)

# Get the temperature values of city: Athens

print ("\nTEMPERATURE\n-----------")

temperature_main = round(loaded_json['main']['temp'] - 274.15,2)

print ("Main temperature is",temperature_main,"°C")

temperature_feel = round(loaded_json['main']['feels_like'] - 274.15,2)

print ("Feel like temperature is",temperature_feel,"°C")

temperature_max = round(loaded_json['main']['temp_max'] - 274.15,2)

print ("Maximum temperature is",temperature_max,"°C")

temperature_min = round(loaded_json['main']['temp_min'] - 274.15,2)

print ("Minimum temperature is",temperature_min,"°C")

# Get the humidity value of city: Athens

print ("\nHUMIDITY\n-----------")

humidity_main = round(loaded_json['main']['humidity'])

print ("Humidity is",humidity_main,"%")

# Get the pressure value of city: Athens

print ("\nPRESSURE\n-----------")

pressure_main = round(loaded_json['main']['pressure'])

print ("Pressure is",pressure_main,"mbar")
