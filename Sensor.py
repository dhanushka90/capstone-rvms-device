class Sensor:
    'public variabe'
    sensorCount = 0

    'constructer'
    def __init__(self, name, output1, output2, output3):
        self.name = name
        self.output1 = output1
        self.output2 = output2
        self.output3 = output3
        Sensor.sensorCount += 1

    def displaysensorcount(self):
        print("Total Sensors: %s" % (Sensor.sensorCount,))

    def displaysensor(self):
        print("Name: ", self.name, " Output A : ", self.output1,
              " Output B :", self.output2, " Output C:", self.output3)
    def output1(self):
        return self.output1();

    def output2(self):
        return self.output2();

    def output3(self):
        return self.output3();







