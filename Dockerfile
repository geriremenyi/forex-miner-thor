FROM python:3.8-slim-buster
WORKDIR /app
EXPOSE 31001

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
ENV PYTHONPATH /app

ENTRYPOINT ["python", "forex_miner_thor/api/api.py"]