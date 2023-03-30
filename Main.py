import json

from Sensor import Sensor
from TempSensor import TempSensor
from GpsSensor import GpsSensor
from GyroAccenoSensor import GyroAccenoSensor
from utils import SchedulerUtils
from utils.ApiUtil import ApiUtil
from utils.DateTimeUtils import DateTimeUtils


class Main:

    def main(self):


        api_utills = ApiUtil



        scheduler = SchedulerUtils

        scheduler.scheule_a_job("Secs", 5,
                                lambda: api_utills.post_req(api_utills, "http://3.97.194.206:8080/api/v1/allSensorData", {
            "timeStamp": DateTimeUtils.getCurrentTimeStamp(self),
            "deviceId":"1",
            "temparature":  TempSensor.get_current_temp(self),
            "accelerometerX": GyroAccenoSensor().get_acc_x(),
            "accelerometerY": GyroAccenoSensor().get_acc_y(),
            "accelerometerZ": GyroAccenoSensor().get_acc_z(),
            "gyroscopeX": GyroAccenoSensor().get_gyro_x(),
            "gyroscopeY": GyroAccenoSensor().get_gyro_y(),
            "gyroscopeZ": GyroAccenoSensor().get_gyro_z(),
            "longitude": GpsSensor().getLongtitude(),
            "latitude" : GpsSensor().getLatitude(),
            "batterystatus": "100%"
        }))


if __name__ == "__main__":
    obj = Main()
    obj.main()
