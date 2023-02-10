
import requests
import json
import config


from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    return "Welcome to the Weather Microservice!, to get the weather in san francisco, type /weather/san-francisco"

@app.get("/weather/{cityname}")
def get_weather() -> str:
    zipcode = requests.get("http://zipode:8001/zipcode/san-francisco").text
    zipcode_list = [int(i) for i in zipcode if i.isdigit()]
    zipcode_int = int("".join(map(str, zipcode_list)))  
    weather_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode_int}&appid={config.api_key}")
    weather = json.loads(weather_response.text)
    return weather['weather'][0]['description']


