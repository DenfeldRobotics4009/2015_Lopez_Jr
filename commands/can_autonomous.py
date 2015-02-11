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

class CanAutonomous(CommandGroup):
    #Should really put some setpoints in. Ehhhhhhh...
    def __init__(self, robot):
        super().__init__()
        auton_generator = [
            DriveStraight(robot, 0, 1, timeout=1),
            CloseClaw(robot), #grabs can
            LiftGoToLevel(robot, 1),
            DriveStraight(robot, 0, 1, timeout=1),

        [self.addSequential(i) for i in auton_generator]