FROM python:3.9

COPY rtu_weather_bot /root/rtu_weather_bot
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
WORKDIR /root/rtu_weather_bot
CMD ["python3", "main.py"]
