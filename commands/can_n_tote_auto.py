__author__ = 'nikolojedison'

from wpilib.command import CommandGroup

from .grab_tote import GrabTote
from .grab_can import GrabCan
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
    """In this one, we grab a can and a tote.
    THIS ISN'T ON THE CAN BUS."""
    #Grab a can, raise lift, drive forward a little, release, lower lift, grab tote, raise lift, turn 90 deg., drive a ways
     def __init__(self, robot):
        super().__init__()
        can_n_tote_gen = [
            LiftGoToLevel(robot, 2),
            GrabCan(robot),
            LiftGoToLevel(robot, 4),
            DriveStraight(robot, 0, -1, timeout=.4)
            LiftGoToLevel(robot, 3),
            OpenClaw(robot),
            GrabTote(robot),
            LiftGoToLevel(robot, 4),
            Turn(robot, 60),
            DriveStraight(robot, 0, -.75, timeout=1.5),
            LiftGoToLevel(robot, 1),
            OpenClaw(robot)]

        #hey, another generator. See commands/can_autonomous.py
        for i in can_n_tote_gen: self.addSequential(i)
