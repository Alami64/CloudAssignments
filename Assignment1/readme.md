**Weather Microservice**
#

A microservice to fetch weather information for a given city.

Requirements

FastAPI
Requests
JSON


To use this microservice, you need to run both zipcodemicroservice server and weathermicroservice server

You can fetch the weather information for a given city by making a GET request to http://127.0.0.1:8001/weather/san-francisco.

The zipcodemicroservice first fetches the zip code for the given city by making a GET request to http://127.0.0.1:8000/zipcode/{city}. It then uses the zip code to make a GET request to the OpenWeatherMap API to fetch the weather information for the city.


