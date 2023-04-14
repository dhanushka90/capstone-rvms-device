import json
import time

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
        deviceId = "1"
        while True:
            get_api_url = "http://3.97.194.206:30080/api/v1/allJourneyRefrigeratorData"
            journyList = api_utills.get_req(self,get_api_url)
            listLength = len(journyList)
            jrId = 0

            for i in range(listLength):
                if journyList[i]["deviceId"] == deviceId and journyList[i]["status"]:
                    jrId = journyList[i]["jrId"]
                    print("Journy ID: ", jrId)
            # do the post api call
            api_utills.post_req(self,
                "http://3.97.194.206:30300/api/v1/allSensorData",
                {
                    "timeStamp": DateTimeUtils.getCurrentTimeStamp(self),
                    "deviceId": deviceId,
                    "jrId": jrId,
                    "temparature": TempSensor.get_current_temp(self),
                    "accelerometerX": GyroAccenoSensor().get_acc_x(),
                    "accelerometerY": GyroAccenoSensor().get_acc_y(),
                    "accelerometerZ": GyroAccenoSensor().get_acc_z(),
                    "gyroscopeX": GyroAccenoSensor().get_gyro_x(),
                    "gyroscopeY": GyroAccenoSensor().get_gyro_y(),
                    "gyroscopeZ": GyroAccenoSensor().get_gyro_z(),
                    "longitude": GpsSensor().getLongtitude(),
                    "latitude": GpsSensor().getLatitude(),
                    "batterystatus": "100%",
                },
            )

            time.sleep(5)
            # wait for 5 sec
            # set isJournyActive = false


if __name__ == "__main__":
    obj = Main()
    obj.main()
