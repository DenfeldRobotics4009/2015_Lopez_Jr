__author__ = 'auxiliary-character'
import threading
import wpilib
import serial
import re
 
class IMUSimple(threading.Thread):
    float_regex = """([\+\-]\d{3}\.\d{2})"""
    int8_regex = """([0-9A-Fa-f]{2})"""
    int16_regex = """([0-9A-Fa-f]{4})"""
    termination_regex = int8_regex + "\n\r"
 
    yprc_packet_regex = re.compile("!y"+
        float_regex+ #Yaw
        float_regex+ #Pitch
        float_regex+ #Roll
        float_regex+ #Compass Heading
        termination_regex)
 
    def _parse(self, line):
        match = yprc_packet_regex.search(line)
        if match:
            groups = match.groups()
            yaw = float(groups[0])
            pitch = float(groups[1])
            roll = float(groups[2])
            compass = float(groups[3])
            return yaw, pitch, roll, compass
 
    def __init__(self):
        self.serial = serial.Serial(0, 57500)
        super().__init__(name="IMU Listener", daemon=True)
        self.start()
        self.mutex = threading.RLock()
        self.yaw = 0.0
        self.pitch = 0.0
        self.roll = 0.0
        self.compass = 0.0
 
    def run(self):
        while True:
            line = self.serial.readline(eol="\n\r")
            yaw, pitch, roll, compass= self._parse(line)
            with self.mutex:
                self.yaw = yaw
                self.pitch = pitch
                self.roll = roll
                self.compass = compass
 
    def getYaw(self):
        with self.mutex:
            return self.yaw
 
    def getPitch(self):
        with self.mutex:
            return self.pitch
 
    def getRoll(self):
        with self.mutex:
            return self.Roll
 
    def getCompass(self):
        with self.mutex:
            return self.compass