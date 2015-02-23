__author__ = 'nikolojedison'

from wpilib.command import CommandGroup

from .close_claw import CloseClaw
from .drive_straight import DriveStraight
from .lift_go_to_level import LiftGoToLevel
from .mecanum_drive_with_joystick import MecanumDriveWithJoystick
from .open_claw import OpenClaw
from .set_claw_setpoint import SetClawSetpoint
from .set_lift_setpoint import SetLiftSetpoint
from .set_mast_setpoint import SetMastSetpoint
from .turn import Turn

class DriveAutonomous(CommandGroup):
    """This is the simple auton."""
    def __init__(self, robot):
        super().__init__()
        #simply drives for a bit. Might be our most valuable asset until we get our turning nailed down.
        self.auton_generator = [DriveStraight(robot, 0, -.5, timeout=5)]

        for i in self.auton_generator: self.addSequential(i)

    def cancel(self):
        for i in self.auton_generator: i._cancel()
        super().cancel()
