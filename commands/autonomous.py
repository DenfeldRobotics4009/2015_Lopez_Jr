__author__ = 'nikolojedison'
#    three_tote = self.smart_dashboard.getBoolean("3 Tote Auto", defaultValue=False)
#    test_switch = self.smart_dashboard.getBoolean("Test Switch", defaultValue=False)

#Also, had no idea what I'd need, so I just imported the commands I thought
#would be useful. *shrugs*
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

class Autonomous(CommandGroup):
    #Should really put some setpoints in. Ehhhhhhh...
    def __init__(self, robot):
        super().__init__()
        self.addSequential(DriveStraight(robot, 0, 1, timeout=1))
        self.addSequential(Turn(robot, -5))
        self.addSequential(CloseClaw(robot)) #grabs first tote
        self.addSequential(LiftGoToLevel(robot, 1))
        self.addSequential(DriveStraight(robot, 0, 1, timeout=1))
        self.addSequential(OpenClaw(robot)) #drops first tote on second tote
        self.addSequential(LiftGoToLevel(robot, 0))
        self.addSequential(CloseClaw(robot)) #grabs second tote
        self.addSequential(LiftGoToLevel(robot, 1))
        self.addSequential(DriveStraight(robot, 0, 1, timeout=1))
        self.addSequential(OpenClaw(robot)) #drops first and second totes on third tote
        self.addSequential(LiftGoToLevel(robot, 0))
        self.addSequential(CloseClaw(robot)) #grabs third tote
        self.addSequential(LiftGoToLevel(robot, 1))
        self.addSequential(Turn(robot, 5))
        self.addSequential(DriveStraight(robot, 0, 1, timeout=1)) #drives around for a bit
