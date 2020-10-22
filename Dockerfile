FROM python:3.8-alpine as base
WORKDIR /app
EXPOSE 5000

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY forex_miner_thor /app

ENTRYPOINT ["python", "api/apy.py"]