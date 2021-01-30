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

        print ("Unsuccessful Request with error code :"+response.status_code)

        return None

weather_json = get_weather_json()

formatted_json = jprint(weather_json)

loaded_json = jload(weather_json)

# Get the temperature values of city: Athens

temperature_main = round(loaded_json['main']['temp'] - 274.15,2)

print ("The main temperature is",temperature_main,"°C")

temperature_max = round(loaded_json['main']['temp_max'] - 274.15,2)

print ("The maximum temperature is",temperature_max,"°C")

temperature_min = round(loaded_json['main']['temp_min'] - 274.15,2)

print ("The minimum temperature is",temperature_min,"°C")
