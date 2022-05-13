import random
import time
from prometheus_client import Gauge, start_http_server

# Used to simulate sensor readings
class Sensor:
    temperature = 0
    relative_humidity = 0.0

    def __init__(self):
        self.cycle()

    def cycle(self):
        self.temperature = random.random() * 100 % 25 # Float between 0 and 25
        self.relative_humidity = random.random()

sensor = Sensor()

g_temp = Gauge('temperature', 'Temperature from sensor')
g_humidity = Gauge('humidity', 'Humidity from sensor')

start_http_server(8000)

while True:
    sensor.temperature

    g_temp.set(round(sensor.temperature, 2))        
    g_humidity.set(round(sensor.relative_humidity, 2))

    time.sleep(2)
    sensor.cycle()