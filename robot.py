#!/usr/bin/env python3
__author__ = 'nikolojedison'
#This code was written to test some things and may end up being used
#on the robot, but I dunno. So far it seems to work fine. Change what
#needs to be changed. Will evolve as time goes on.
#-Nik Mal

import wpilib
from wpilib.command import Scheduler
from oi import OI

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
        self.drivetrain.drive.setSafetyEnabled(True)
        while self.isOperatorControl() and self.isEnabled():
            Scheduler.getInstance().run()
            wpilib.Timer.delay(.005)    # don't burn up the cpu

    def disabled(self):
        pass

    def test(self):
        """no tests yet, woo"""
        pass

    def log(self):
        self.camera.log()
        self.derailer.log()
        self.drivetrain.log()
        self.lift.log()
        self.grabber.log()
        self.mast.log()

if __name__ == "__main__":
    wpilib.run(Lopez_Jr)
