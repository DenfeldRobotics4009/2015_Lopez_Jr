#!/usr/bin/env python3
__author__ = 'nikolojedison'
#This code was written to test some things and may end up being used
#on the robot, but I dunno. So far it seems to work fine. Change what
#needs to be changed. Will evolve as time goes on.
#-Nik Mal

from networktables import NetworkTable
import wpilib
import logging
from autonomous_utilities import Auto
from drive_control import *

from subsystems.camera import Camera
from subsystems.derailer import Derailer
from subsystems.drivetrain import Drivetrain
from subsystems.lift import Lift
from subsystems.grabber import Grabber
from subsystems.mast import Mast

logging.basicConfig(level=logging.DEBUG)

class Lopez_Jr(wpilib.SampleRobot):
    def robotInit(self):
        """initialises robot as a mecanum drive bot w/ 2 joysticks and a camera"""
        #want to change this to Xbox 360 controller eventually... probably sooner rather
        #than later.

        #self.gyro = wpilib.Gyro(0)

        self.aux_left = wpilib.Jaguar(6) #just goes in subsys - need to find out what they do
        self.aux_right = wpilib.Jaguar(4)
        self.window_motor = wpilib.Jaguar(5)

        self.grabba_pot = wpilib.AnalogPotentiometer(1)
        self.lift_pot = wpilib.AnalogPotentiometer(2)

        def aux_combined(output):
            """use for PID control"""
            self.aux_left.pidWrite(output)
            self.aux_right.pidWrite(output)


    def autonomousInit(self):
        """Woo, auton code. Needs to be tested."""
        self.autonomousCommand.start()


    def operatorControl(self): #Should this go in oi.py?
        """Runs the drive with mecanum steering. Other motors added as needed."""

        self.drive.setSafetyEnabled(True)

        while self.isOperatorControl() and self.isEnabled():
            precision = self.stick_right.getRawButton(0)
            x = drive_control(self.stick_right.getX(), precision)
            y = drive_control(self.stick_right.getY(), precision)
            z = drive_control(self.stick_right.getZ(), precision)

            aux = dead_zone(self.stick_left.getY(), .1)
            window_motor = dead_zone(self.stick_left.getX(), .1)
            #self.smart_dashboard.putNumber("Gyro",self.gyro.getAngle())

            gyro_angle = 0

            self.drive.mecanumDrive_Cartesian(x, y, z, 0)   # mecanum drive

            self.aux_left.set(aux) # auxiliary left miniCIM
            self.aux_right.set(aux)# auxiliary right miniCIM
            self.window_motor.set(window_motor) # random window motor that electrical hooked up
            wpilib.Timer.delay(.005)    # don't burn up the cpu

    def disabled(self):
        pass

    def test(self):
        """no tests yet, woo"""
        pass

if __name__ == "__main__":
    wpilib.run(Lopez_Jr)
