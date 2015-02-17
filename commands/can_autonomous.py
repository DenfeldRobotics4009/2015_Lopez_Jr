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
from .lift_go_to_level import LiftGoToLevel

class CanAutonomous(CommandGroup):
    """This is the autonomous where we grab the can and drive off with it."""
    #Should really put some setpoints in. Ehhhhhhh...
    #Clamp, lift up, turn 45 deg left, go forward, drop can
    def __init__(self, robot):
        super().__init__()
        auton_generator = [
            LiftGoToLevel(robot, 2),
            GrabTote(robot), #grabs can
            LiftGoToLevel(robot, 4),
            DriveStraight(robot, 0, -.5, timeout=1),
            Turn(robot, 60),
            DriveStraight(robot, 0, -.5, timeout=2.5),
            LiftGoToLevel(robot, 2),
            OpenClaw(robot), #drops can
            DriveStraight(robot, 0, .5, timeout=.25)]

        for i in auton_generator: self.addSequential(i)
