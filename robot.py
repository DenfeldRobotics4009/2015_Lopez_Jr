#!/usr/bin/env python3
__author__ = 'nikolojedison'
#This code was written to test some things and may end up being used
#on the robot, but I dunno. So far it seems to work fine. Change what
#needs to be changed. Will evolve as time goes on.
#-Nik Mal

import wpilib
from wpilib.command import Scheduler
from oi import OI

#from subsystems.camera import Camera
from subsystems.derailer import Derailer
from subsystems.drivetrain import Drivetrain
from subsystems.lift import Lift
from subsystems.claw import Claw
from subsystems.mast import Mast

from commands.three_tote_autonomous import ThreeToteAutonomous
from drive_control import dead_zone

class Lopez_Jr(wpilib.SampleRobot):
    def robotInit(self):
        """initialises robot as a mecanum drive bot w/ 2 joysticks and a camera"""

#        self.camera = Camera(self)
        self.derailer = Derailer(self)
        self.drivetrain = Drivetrain(self)
        self.lift = Lift(self)
        self.claw = Claw(self)
        self.mast = Mast(self)
        self.oi = OI(self)

        self.ThreeToteAutonomousCommand = ThreeToteAutonomous(self)

    def autonomous(self):
        """Woo, auton code. Needs to be tested."""

        self.drivetrain.drive.setSafetyEnabled(False)
        
        if self.oi.smart_dashboard.getBoolean("3 Tote Auto"):
            self.ThreeToteAutonomousCommand.start()
        
        elif self.oi.smart_dashboard.getBoolean("Can Auto"):
            self.CanAutonomousCommand.start()
            
        else:
            self.DriveAutonomousCommand.start()

        while self.isAutonomous() and self.isEnabled():
            Scheduler.getInstance().run()
            self.log()
            wpilib.Timer.delay(.005)    # don't burn up the cpu


    def operatorControl(self):
        """Runs the drive with mecanum steering. Other motors added as needed."""
        self.ThreeToteAutonomousCommand.cancel()
        self.CanAutonomousCommand.cancel()
        self.DriveAutonomousCommand.cancel()
        self.drivetrain.drive.setSafetyEnabled(True)
        joystick = self.oi.getJoystickLeft()
        while self.isOperatorControl() and self.isEnabled():
            self.log()
            Scheduler.getInstance().run()
            #if joystick.getRawButton(7):
            #    self.lift.motor.set(dead_zone(self.oi.getJoystickLeft().getThrottle(), .1))
            #else:
            #    self.lift.motor.set(0)
            #if joystick.getRawButton(9):
            #    self.mast.motor.set(dead_zone(self.oi.getJoystickLeft().getThrottle(), .1)*.35)
            #else:
            #    self.mast.motor.set(0)
            #if joystick.getRawButton(11):
            #    self.grabber.motor.set(dead_zone(self.oi.getJoystickLeft().getThrottle(), .1))
            #else:
            #    self.grabber.motor.set(0)
        wpilib.Timer.delay(.005)    # don't burn up the cpu


    def disabled(self):
        self.ThreeToteAutonomousCommand.cancel()
        self.CanAutonomousCommand.cancel()
        self.DriveAutonomousCommand.cancel()
        while self.isDisabled():
            self.log()

    def test(self):
        """no tests yet, woo"""
        pass

    def log(self):
#        self.camera.log()
        self.derailer.log()
        self.drivetrain.log()
        self.lift.log()
        self.claw.log()
        self.mast.log()

if __name__ == "__main__":
    wpilib.run(Lopez_Jr)
