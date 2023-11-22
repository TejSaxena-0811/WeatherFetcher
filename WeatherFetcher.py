# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 20:54:43 2023

@author: jaigurudev
"""

import requests

API_KEY = "fa633aaeb3daaa88255e8974c4ea8d89"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:        #  200 means success. 404 means error. 
    data = response.json()
    #print(data)                        # this will print out *all* the information.
    weather = data['weather'][0]['description']
    print("Weather: " , weather)
    temperature = data['main']['temp']      #  this will be in kelvin.
    celsius = temperature - 273.15
    print("Temperature: " , round(celsius , 2) , "°C")
else:
    print("An error occured my friend.")
