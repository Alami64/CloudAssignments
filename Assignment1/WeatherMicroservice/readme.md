To run this service, we type "uvicorn weatherservice:app --reload --port 8001"

if we are using docker, then we first want to build an image using :

"docker build -t weatherapp ."

Then the next step is to create a network named weatherapp using "docker network create weathernet"

and then you run the container using this command "docker run --net weathernet  -p 8001:8001 --name weathercode weatherapp"

