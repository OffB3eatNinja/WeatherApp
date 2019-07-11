from fp_model import WeatherReport
from geopy.geocoders import Nominatim
import requests

API_KEY="89bfd529e419ae907537751129425e41"
#option_list = "exclude=currently,minutely,hourly,alerts&amp;units=si"
class Weather_Controller:
    def getLocation(self, location_info):
        location = Nominatim().geocode(location_info, language='en_US')
        return location

    def getWeatherInfo(self,data,location):
        latitude = str(location.latitude)
        longitude = str(location.longitude)
        weather_reports = []
        response=requests.get("https://api.darksky.net/forecast/"+API_KEY+"/"+latitude+","+longitude)
        json_response=response.json()
        unit_type = '°F' if json_response['flags']['units'] == 'us' else '°C'
        min_temperature = str(json_response['daily']['data'][0]['apparentTemperatureMin']) + unit_type
        max_temperature = str(json_response['daily']['data'][0]['apparentTemperatureMax']) + unit_type
        summary = json_response['daily']['data'][0]['summary']
        icon = json_response['daily']['data'][0]['icon']
        precip_type = None
        precip_prob = None
        raining_chance = None
        if 'precipProbability' in json_response['daily']['data'][0] and 'precipType' in json_response['daily']['data'][0]:
            precip_type = json_response['daily']['data'][0]['precipType']
            precip_prob = json_response['daily']['data'][0]['precipProbability']
        if (precip_type == 'rain' and precip_prob != None):
            precip_prob *= 100
            raining_chance = "Chance of rain: %.2f%%" % (precip_prob)

        wr = WeatherReport( max_temperature, min_temperature,
                               summary, raining_chance, icon)
        weather_reports.append(wr)
        return weather_reports
