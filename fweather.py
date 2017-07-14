#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import json
import requests


class FWeather(object):
    def __init__(self):
        if os.path.isfile(os.path.join(os.environ.get('HOME'), '.config', 'forecastio.json')):
            with open(os.path.join(os.environ.get('HOME'), '.config', 'forecastio.json'), 'r') as f:
                self.api_key = json.load(f)
                self.api_key = self.api_key.get('token', None)
        elif os.environ.get('FORECASTIO_KEY'):
            self.api_key = os.environ.get('FORECASTIO_KEY', None)
        else:
            self.api_key = None

    def _get_location_info(self):
        r = requests.get('http://ip-api.com/json')
        return r.json()

    def _get_current_weather_info(self, lat, lon):
        r = requests.get('https://api.darksky.net/forecast/{}/{},{}'.format(self.api_key, lat, lon))
        weather_json = r.json()
        return weather_json['currently']

    def _get_icon(self, condition):
        icon_map = {
            "clear-day": "☀",
            "clear-night": "🌙",
            "rain": "🌧",
            "snow": "🌨",
            "sleet": "🌨",
            "wind": "🌬",
            "fog": "🌫",
            "cloudy": "🌥",
            "partly-cloudy-day": "🌤",
            "partly-cloudy-night": "🌙☁️",
            "hail": "⛔🌨⛔",
            "thunderstorm": "⛔⛈⛔",
            "tornado": "⛔🌪⛔",
        }
        return icon_map.get(condition, "❓")

    def get_weather(self):
        location = self._get_location_info()

        city = location['city']
        weather_info = self._get_current_weather_info(lat=location['lat'], lon=location['lon'])

        if self.api_key is None:
            # No API key is configured. Let the user know.
            print("💀 No API key 💀")
        else:
            print("{city}: {condition_icon}  {condition} {temperature}°F {windspeed}mph").format(
                city=city,
                condition_icon=self._get_icon(condition=weather_info['icon']),
                condition=weather_info['summary'],
                temperature=weather_info['temperature'],
                windspeed=weather_info['windSpeed'],
            )

if __name__ == '__main__':
    FWeather().get_weather()
