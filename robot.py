#!/usr/bin/env python3
__author__ = 'nikolojedison'
#This code seems to work fine. Change what
#needs to be changed. Will evolve as time goes on.
#-Nik Mal

#These are the WPILib section
import wpilib
import networktables
from wpilib.command import Scheduler
from oi import OI

#This is all the subsystems
from subsystems.drivetrain import Drivetrain
from subsystems.lift import Lift
from subsystems.claw import Claw
from subsystems.mast import Mast

#This is all the commands
from commands.three_tote_autonomous import ThreeToteAutonomous
from commands.can_autonomous import CanAutonomous
from commands.drive_autonomous import DriveAutonomous

#This is all the special drive stuff
from drive_control import dead_zone

class Lopez_Jr(wpilib.SampleRobot):
    def robotInit(self):
        """Initialises 'bot w/ all subsystems (derailer needs testing) and joysticks"""

        self.drivetrain = Drivetrain(self)
        self.lift = Lift(self)
        self.claw = Claw(self)
        self.mast = Mast(self)
        self.oi = OI(self)

        #These are self-describing.
        self.ThreeToteAutonomousCommand = ThreeToteAutonomous(self)
        self.CanAutonomousCommand = CanAutonomous(self)
        self.DriveAutonomousCommand = DriveAutonomous(self)

    def autonomous(self):
        """Woo, auton code w/ 3 modes. Needs to be tested."""

        self.drivetrain.drive.setSafetyEnabled(False)

        if self.oi.smart_dashboard.getBoolean("3 Tote Auto"):
            self.ThreeToteAutonomousCommand.start()
            print("3 tote auto started")

        elif self.oi.smart_dashboard.getBoolean("Can Auto"):
            self.CanAutonomousCommand.start()
            print("Can Auto started")

        else:
            self.DriveAutonomousCommand.start()
            print("Drive Auto started")

        while self.isAutonomous() and self.isEnabled():
            Scheduler.getInstance().run()
            self.log()
            wpilib.Timer.delay(.005)    # don't burn up the cpu


    def operatorControl(self):
        """Runs the 'bot with a joystick - dunno why we don't have both."""
        self.ThreeToteAutonomousCommand.cancel()
        self.CanAutonomousCommand.cancel()
        self.DriveAutonomousCommand.cancel()
        self.drivetrain.drive.setSafetyEnabled(True)
        joystick = self.oi.getJoystickLeft() #Do we even need this?
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
        """Stuff to do when the 'bot is disabled"""
        self.ThreeToteAutonomousCommand.cancel()
        self.CanAutonomousCommand.cancel()
        self.DriveAutonomousCommand.cancel()
        while self.isDisabled():
            self.log()

    def test(self):
        """There aren't any tests."""
        pass

    def log(self):
        """Woo, logging."""
        self.drivetrain.log()
        self.lift.log()
        self.claw.log()
        self.mast.log()

if __name__ == "__main__":
    wpilib.run(Lopez_Jr)
