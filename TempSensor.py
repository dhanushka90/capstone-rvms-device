from Sensor import Sensor


from w1thermsensor import W1ThermSensor
from random import seed
from random import randint


class TempSensor(Sensor):

    def get_current_temp(self):
        sensor = W1ThermSensor()
        temp = sensor.get_temperature()
        print(temp)
        return temp

    def get_mock_current_temp(self):
        seed(1)
        temp = randint(0, 25)
        return temp




