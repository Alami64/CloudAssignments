FROM python:3.10

WORKDIR /WeatherMicroservice

EXPOSE 8001

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "weatherservice:app", "--host", "0.0.0.0", "--port", "8001"]

