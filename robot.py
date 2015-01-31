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

class Lopez_Jr(wpilib.SampleRobot):
    def robotInit(self):
        """initialises robot as a mecanum drive bot w/ 2 joysticks and a camera"""
        
        self.camera = Camera(self)
        self.derailer = Derailer(self)
        self.drivetrain = Drivetrain(self)
        self.lift = Lift(self)
        self.grabber = Grabber(self)
        self.mast = Mast(self)
        self.oi = OI(self)
        
        self.autonomousCommand = Autonomous(self)

    def autonomous(self):
        """Woo, auton code. Needs to be tested."""
        
        self.autonomousCommand.start()
        
        while self.isAutonomous() and self.isEnabled():
            Scheduler.getInstance().run()
            wpilib.Timer.delay(.005)    # don't burn up the cpu


    def operatorControl(self):
        """Runs the drive with mecanum steering. Other motors added as needed."""
        self.drive.setSafetyEnabled(True)
        wpilib.Timer.delay(.005)    # don't burn up the cpu

    def disabled(self):
        pass

    def test(self):
        """no tests yet, woo"""
        pass

if __name__ == "__main__":
    wpilib.run(Lopez_Jr)
