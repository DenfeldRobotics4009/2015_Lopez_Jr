__author__ = 'nikolojedison'
from wpilib.command import Subsystem
import wpilib

class Camera(Subsystem):

    def __init__(self, robot):
        #This is for a USB camera. Uncomment it if we aren't using the Axis.
        self.camera = wpilib.USBCamera()
        self.camera.setExposureManual(50)
        self.camera.setBrightness(80)
        self.camera.updateSettings()
        self.camera.setFPS(10)
        self.camera.setSize(320, 240)
        self.camera.setWhiteBalanceAuto()
        #self.camera.setQuality(30)

        server = wpilib.CameraServer.getInstance()
        server.startAutomaticCapture(self.camera)

    def initDefaultCommand(self):
        pass

    def log(self):
        pass
