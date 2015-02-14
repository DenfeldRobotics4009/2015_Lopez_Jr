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

class ThreeToteAutonomous(CommandGroup):
    #Should really put some setpoints in. Ehhhhhhh...
    def __init__(self, robot):
        super().__init__()
        auton_generator = [
            DriveStraight(robot, 0, -.75, timeout=1),
            Turn(robot, -5),
            CloseClaw(robot), #grabs first tote
            LiftGoToLevel(robot, 1),
            DriveStraight(robot, 0, -.75, timeout=1),
            OpenClaw(robot), #drops first tote on second tote
            LiftGoToLevel(robot, 0),
            CloseClaw(robot), #grabs second tote
            LiftGoToLevel(robot, 1),
            DriveStraight(robot, 0, -.75, timeout=1),
            OpenClaw(robot), #drops first and second totes on third tote
            LiftGoToLevel(robot, 0),
            CloseClaw(robot), #grabs third tote
            LiftGoToLevel(robot, 1),
            Turn(robot, 5),
            DriveStraight(robot, 0, -.75, timeout=1)] #drives around for a bit

        for i in auton_generator: self.addSequential(i)
