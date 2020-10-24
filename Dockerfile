FROM python:3.8-buster
WORKDIR /app
EXPOSE 31001

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

ENTRYPOINT ["python", "forex_miner_thor/api/api.py"]