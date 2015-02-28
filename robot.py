#!/usr/bin/env python3
__author__ = 'nikolojedison'

#These are the WPILib libraries.
import wpilib
import networktables
from wpilib.command import Scheduler
from oi import OI

#These are all the subsystems.
from subsystems.drivetrain import Drivetrain
from subsystems.lift import Lift
from subsystems.claw import Claw
from subsystems.mast import Mast
#from subsystems.winch import Winch #still tenative

#These are all the autons.
from commands.can_autonomous import CanAutonomous
from commands.can_n_tote_auto import CanNToteAuto
from commands.drive_autonomous import DriveAutonomous
from commands.three_tote_autonomous import ThreeToteAutonomous
from commands.tote_autonomous import ToteAutonomous
from commands.play_macro import PlayMacro

#This is all the special drive stuff we need. Yay, libraries.
from drive_control import dead_zone

class Lopez_Jr(wpilib.SampleRobot):
    def robotInit(self):
        """Initialises 'bot w/ all subsystems (derailer needs testing) and joysticks"""

        #Subsystem initialisation.  Woo.
        self.drivetrain = Drivetrain(self)
        self.lift = Lift(self)
        self.claw = Claw(self)
        self.mast = Mast(self)
#        self.winch = Winch(self)
        self.oi = OI(self)

        #These are self-describing autonomouses. Waaaaaait... Autono-mouse?
        self.ThreeToteAutonomousCommand = ThreeToteAutonomous(self)
        self.CanAutonomousCommand = CanAutonomous(self)
        self.CanNToteAutoCommand = CanNToteAuto(self)
        self.DriveAutonomousCommand = DriveAutonomous(self)
        self.ToteAutonomousCommand = ToteAutonomous(self)
        self.PlayMacroCommand = PlayMacro(self, "macro.csv")

    def autonomous(self):
        """Woo, auton code w/ 3 modes. Needs to be tested."""
        #Still tenative if we're using anything other than our macro.
        #May have to consult with Drive Team and Coach.
        self.drivetrain.drive.setSafetyEnabled(False)

        try:
            if self.oi.smart_dashboard.getBoolean("3 Tote Auto"):
                self.ThreeToteAutonomousCommand.start()
                print("3 Tote Auto started")

            elif self.oi.smart_dashboard.getBoolean("Can Auto"):
                self.CanAutonomousCommand.start()
                print("Can Auto started")

            elif self.oi.smart_dashboard.getBoolean("Can/Tote Auto"):
                self.CanNToteAutoCommand.start()
                print("Can and Tote Auto started")

            elif self.oi.smart_dashboard.getBoolean("Tote Auto"):
                self.ToteAutonomousCommand.start()
                print("Tote Auto started")

            elif self.oi.smart_dashboard.getBoolean("Play Macro"):
                self.PlayMacroCommand.start()
                print("Macro replay started")

            elif self.oi.smart_dashboard.getBoolean("Drive Auto"):
                self.DriveAutoCommand.start()
                print("Drive Auto started")

            else:
                pass

        except KeyError:
            pass

        while self.isAutonomous() and self.isEnabled():
            Scheduler.getInstance().run()
            self.log()
            wpilib.Timer.delay(.005)    # don't burn up the cpu


    def operatorControl(self):
        """Runs the 'bot with the fancy joystick and an awesome gamepad THAT IS AWESOME."""

        #Cancel the autons - that could go badly otherwise.
        self.ThreeToteAutonomousCommand.cancel()
        self.CanAutonomousCommand.cancel()
        self.DriveAutonomousCommand.cancel()
        self.ToteAutonomousCommand.cancel()
        self.PlayMacroCommand.cancel()
        self.CanNToteAutoCommand.cancel()

        #More stuff.
        self.drivetrain.drive.setSafetyEnabled(True)
        joystick = self.oi.getJoystickLeft() #Do we even need this?

        #Run the Scheduler and the timer. Usefulness, yay.
        while self.isOperatorControl() and self.isEnabled():
            self.log() #It's log, it's log, it's not big or heavy or wood.
            Scheduler.getInstance().run()
            wpilib.Timer.delay(.005)    # don't burn up the cpu


    def disabled(self):
        """Stuff to do when the 'bot is disabled"""

        #cancel the autons IN THE NAME OF SAFETY
        self.ThreeToteAutonomousCommand.cancel()
        self.CanAutonomousCommand.cancel()
        self.DriveAutonomousCommand.cancel()
        self.ToteAutonomousCommand.cancel()
        self.PlayMacroCommand.cancel()
        self.CanNToteAutoCommand.cancel()

        while self.isDisabled():
            self.log() #It's log, it's log, it's better than bad, it's good.
            wpilib.Timer.delay(.005)

    def test(self):
        """There aren't any tests."""
        pass

    def log(self):
        """Woo, logging."""
        self.drivetrain.log()
        self.lift.log()
        self.claw.log()
        self.mast.log()
#        self.winch.log()

if __name__ == "__main__":
    wpilib.run(Lopez_Jr)
