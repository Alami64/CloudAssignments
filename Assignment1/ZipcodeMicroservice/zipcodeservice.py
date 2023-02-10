import json
from fastapi import FastAPI
import requests




app = FastAPI()

    
@app.get("/zipcode/{city}")
def get_zip_code(city:str) -> str:
    city = city.replace("-", "%20")
    response = requests.get(f"https://app.zipcodebase.com/api/v1/code/city?apikey=4658d420-a84e-11ed-a65a-4b41c5a0c15e&city={city}&country=us")
    zip_code = json.loads(response.text)["results"][0]
    return zip_code




    
    
