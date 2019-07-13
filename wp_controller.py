from fp_model import WeatherReport
from geopy.geocoders import Nominatim
import requests

API_KEY="89bfd529e419ae907537751129425e41"
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
        unit = '°F' if json_response['flags']['units'] == 'us' else '°C'
        min_temperature = str(json_response['daily']['data'][0]['apparentTemperatureMin']) + unit
        max_temperature = str(json_response['daily']['data'][0]['apparentTemperatureMax']) + unit
        summary = json_response['daily']['data'][0]['summary']
        icon = json_response['daily']['data'][0]['icon']
        precip_type = None
        precip_prob = None
        raining_prob = None
        if 'precipProbability' in json_response['daily']['data'][0] and 'precipType' in json_response['daily']['data'][0]:
            precip_type = json_response['daily']['data'][0]['precipType']
            precip_prob = json_response['daily']['data'][0]['precipProbability']
        if (precip_type == 'rain' and precip_prob != None):
            precip_prob *= 100
            raining_prob = "Chance of rain: %.2f%%" % (precip_prob)

        wr = WeatherReport( max_temperature, min_temperature,
                               summary, raining_prob, icon)
        weather_reports.append(wr)
        return weather_reports
