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

class CanNToteAuto(CommandGroup):
    """In this one, we grab a can and a tote."""
    #Grab a can, raise lift, drive forward a little, release, lower lift, grab tote, raise lift, turn 90 deg., drive a ways
     def __init__(self, robot):
        super().__init__()
        can_n_tote_gen = [
            GrabCan(robot),
            LiftStuff(robot, .75, 2),
            DriveStraight(robot, 0, -.5, timeout=.25),
            OpenClaw(robot),
            LiftStuff(robot, -.75, 2),
            GrabTote(robot),
            LiftStuff(robot, .75, .5),
            Turn(robot, 90),
            DriveStraight(robot, 0, -1, timeout=.25),
        ]
