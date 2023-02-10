FROM python:3.10

WORKDIR /ZipcodeMicroservice

EXPOSE 8000

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "zipcodeservice:app", "--host", "0.0.0.0", "--port", "8000"]