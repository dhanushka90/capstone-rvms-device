from Sensor import Sensor
import os
import sys
import time
import smbus

from imusensor.MPU9250 import MPU9250


class GyroAccenoSensor(Sensor):

    def __init__(self):
        self.accelX = 0
        self.accelY = 0
        self.accelZ = 0
        self.gyroX = 0
        self.gyroY = 0
        self.gyroZ = 0

        self.initialize_gyro_acceno_sensor()

    def initialize_gyro_acceno_sensor(self):
        address = 0x68
        bus = smbus.SMBus(1)
        imu = MPU9250.MPU9250(bus, address)
        imu.begin()
        print(
            "Accel x: {0} ; Accel y : {1} ; Accel z : {2}".format(imu.AccelVals[0], imu.AccelVals[1], imu.AccelVals[2]))
        print("Gyro x: {0} ; Gyro y : {1} ; Gyro z : {2}".format(imu.GyroVals[0], imu.GyroVals[1], imu.GyroVals[2]))

        self.accelX = imu.AccelVals[0]
        self.accelY = imu.AccelVals[1]
        self.accelZ = imu.AccelVals[2]

        self.gyroX = imu.GyroVals[0]
        self.gyroY = imu.GyroVals[1]
        self.gyroZ = imu.GyroVals[2]

    def get_acc_x(self):
        return str(self.accelX)

    def get_acc_y(self):
        return str(self.accelY)

    def get_acc_z(self):
        return str(self.accelZ)

    def get_gyro_x(self):
        return str(self.gyroX)

    def get_gyro_y(self):
        return str(self.gyroY)

    def get_gyro_z(self):
        return str(self.gyroZ)
