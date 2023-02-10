
To run this service, we type "uvicorn zipcodeservice:app --reload --port 8000"

if we are using docker, then we first want to build an image using :

"docker build -t zipcodeapp ."

Then the next step is to create a network named weatherapp using "docker network create weathernet", if we already created it, it will say that there is already a network with that nam, so we can just skip ahead.

and then you run the container using this command "docker run --net weathernet -p 8000:8000 --name zipcode zipcodeapp"
