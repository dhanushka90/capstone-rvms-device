from Sensor import Sensor
from gps import *


class GpsSensor(Sensor):

    def __init__(self):
        self.lat = 0
        self.lan = 0
        self.is_gps_cordinates_available()

    def is_gps_cordinates_available(self):

        gpsd = gps(mode=WATCH_ENABLE | WATCH_NEWSTYLE)
        while True:
            nx = gpsd.next()
            if nx['class'] == 'TPV':
                latitude = getattr(nx, 'lat', "Unknown")
                longitude = getattr(nx, 'lon', "Unknown")
                print("Cordinates(lat,lan) = " + str(latitude) + "," + str(longitude))

                self.lat = str(latitude)
                self.lon = str(longitude)

                break

    def getLatitude(self):
        return self.lat

    def getLongtitude(self):
        return self.lon
