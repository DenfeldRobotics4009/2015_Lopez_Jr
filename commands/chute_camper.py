__author__ = 'nikolojedison'

from wpilib.command import CommandGroup

from .grab_tote import GrabTote
from .drive_straight import DriveStraight
from .lift_go_to_level import LiftGoToLevel
from .mecanum_drive_with_joystick import MecanumDriveWithJoystick
from .open_claw import OpenClaw
from .set_claw_setpoint import SetClawSetpoint
from .set_lift_setpoint import SetLiftSetpoint
from .set_mast_setpoint import SetMastSetpoint
from .turn import Turn
from .lift_stuff import LiftStuff

class ChuteCamper(CommandGroup):
    """This one camps at the chute like a little n00b. Seriously though, I have no idea why we're doing this."""
        def __init__(self, robot):
            super().__init__()