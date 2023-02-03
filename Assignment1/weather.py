import requests
import json
import http.server
import config 



class WeatherHandler(http.server.BaseHTTPRequestHandler):
    def _send_response(self, message):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(message, "utf16"))

    def do_GET(self):
        if 'city' in self.path:
            city = self.path.split('=')[1]
            weather = self.get_city_weather(city)
            coord = weather['coord']
            longitude = coord['lon']
            latitude = coord['lat']

            main = weather['main']
            temp = main['temp']
            feels_like = main['feels_like']
            pressure = main['pressure']
            humidity = main['humidity']

            wind = weather['wind']
            speed = wind['speed']
            degree = wind['deg']

            clouds = weather['clouds']['all']

            message = f"The weather in {city}:\n"
            message += f"\nLongitude: {longitude}°, Latitude: {latitude}°\n"
            message += f"\nTemperature: {temp - 273.15:.2f}°C, Feels like: {feels_like - 273.15:.2f}°C\n"
            message += f"\nPressure: {pressure} hPa, Humidity: {humidity}%\n"
            message += f"\nWind Speed: {speed:.2f} m/s, Degree: {degree}°\n"
            message += f"\nClouds: {clouds}%"

            self._send_response(message)
        else:
            message = 'Please enter a city name in the URL, e.g. http://localhost:8000/city=san-francisco'
            self._send_response(message)


    def get_zip_code(self,city):
        
        response = requests.get(f"https://www.zipcodeapi.com/rest/DemoOnly00T9TlNMaZIPoG6Z81oPYYCUF8EkrAmhdri9QZIj2zXaLg3vU5sQAIFG/city-zips.json/{city}/CA")
        zip_code = json.loads(response.text)['zip_codes']
        if len(zip_code) > 0:
            zip_code = zip_code[0]
        else:
            return self.get_zip_code("san-francisco")
        return zip_code


    def get_weather(self,zip_code):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code}&appid={config.api_key}")
        weather = json.loads(response.text)
        return weather
    
    def get_city_weather(self,city):
        zip_code = self.get_zip_code(city)
        weather = self.get_weather(zip_code)
        return weather
    
def run():
    server_address = ('localhost', 8000)
    httpd = http.server.HTTPServer(server_address, WeatherHandler)
    print('Starting server on http://localhost:8000')
    httpd.serve_forever()


def main():
    run()


if __name__ == "__main__":
    main()