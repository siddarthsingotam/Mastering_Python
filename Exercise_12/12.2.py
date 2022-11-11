import requests
# import json

# My api_key = "794bc234d44ce063d594d5840c40263d" -Free usage Plan

# Taking Input from Front-end user
api_key = input(f"\nEnter your API key here: ")
city_name = input(f"Enter City name to find info: ").capitalize()

# Processing request using Open Weather API server
request = "https://api.openweathermap.org/data/2.5/weather?q=" + city_name + f"&appid={api_key}"
response = requests.get(request).json()
# print(json.dumps(response, indent=2))

# Getting Desired information from API
temp_in_kelvin = response["main"]["temp"]
description = response["weather"][0]["description"]

celsius = int(temp_in_kelvin) - 275.15
print(f"The city is: {city_name}, Temperature: {round(celsius, 1)} Celsius. The weather condition is: {description}.")
