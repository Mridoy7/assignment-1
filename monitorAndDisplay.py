# assignment-1
import time
import json
from w1thermsensor import W1ThermSensor




with open('config.json') as f:
  data = json.load(f)

print(data)

sensor = W1ThermSensor()

while True:
    temperature = sensor.get_temperature()

    if temperature < data['cold_max']:
        #display temperature with blue colour
    elif temperature >= data['comfortable_mix'] or temperature <= data['comfortable_max']:
        #display temperature with green colour.
    elif temperature >data['hot_min']:
        #display temperature with red colour

    time.sleep(10)



