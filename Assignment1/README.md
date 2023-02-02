
City Name -> Weather Generator Microservice
=======
Introduction
----------- 
This is a simple weather application that returns the current weather in a specified city. 
The application uses the OpenWeatherMap API to get weather information and the Zipcode API to get the zip code for a city.
This application takes a city name as input in the form of e.g "san-francisco" and return a formatted json response that provides a weather report
fo the given city. The app uses two microservices that are wrapped under a class WeatherHandler wrapper. 

Steps to Write the Weather Program
-----------
1. Import the required libraries (requests, json, http.server)
2. Create a handler class (WeatherHandler) that inherits from http.server.BaseHTTPRequestHandler.
3. Implement the do_GET method to handle GET requests.
4. Within the do_GET method, extract the city name from the URL.
5. Get the zip code for the city using the get_zip_code method.
6. Use the zip code to get the weather information from the OpenWeatherMap API using the get_weather method.
7. Format the weather information into a message and send it as a response to the browser.
8. Implement the run method to start the HTTP server.
9. Call the run method within the main method.


Usage
-----------
To use the application, run the weather.py file and access http://localhost:8000 in a web browser. To get the weather for a specific city, add the city name to the URL, for example: http://localhost:8000/city=san-francisco. 
If the city name is not valid or a zipcode was not generatde, the weather for San Francisco will be returned by default.

Using Docker
-----------
The application is containerized using Docker. To build the image, run the following command in the root directory of the application:

>docker build -t weather-app .

To run the container use following command:

>docker run -p 8000:8000 weather-app

The application will then be accessible at http://localhost:8000.

