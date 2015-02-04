__author__ = 'nikolojedison'
#Temporary copypasta from robot.py, since I'm doing some housekeeping
#over there. -Nik    
#    three_tote = self.smart_dashboard.getBoolean("3 Tote Auto", defaultValue=False) 
#    test_switch = self.smart_dashboard.getBoolean("Test Switch", defaultValue=False)

#Also, had no idea what I'd need, so I just imported the commands I thought
#would be useful. *shrugs*
from .close_grabba import CloseGrabba
from .drive_straight import DriveStraight
from .lift_go_to_level import LiftGoToLevel
from .mecanum_drive_with_joystick import MecanumDriveWithJoystick
from .open_grabba import OpenGrabba
from .set_grabba_setpoint import SetGrabbaSetpoint
from .set_lift_setpoint import SetLiftSetpoint
from .set_mast_setpoint import SetMastSetpoint
    
class Autonomous(CommandGroup):
    #Should really put some setpoints in. Ehhhhhhh...
    def __init___(self, robot)
        super().__init__()
        self.addSequential(DriveStraight(robot))
        self.addSequential(SetGrabbaSetpoint(robot, 1))
        self.addSequential(CloseGrabba(robot)) #grabs first tote
        self.addSequential(SetLiftSetpoint(robot, 1))
        self.addSequential(LiftGoToLevel(robot))
        self.addSequential(DriveStraight(robot))
        self.addSequential(OpenGrabba(robot)) #drops first tote on second tote
        self.addSequential(SetLiftSetpoint(robot, -1))
        self.addSequential(LiftGoToLevel(robot))
        self.addSequential(CloseGrabba(robot)) #grabs second tote
        self.addSequential(SetLiftSetpoint(robot, 2))
        self.addSequential(LiftGoToLevel(robot))
        self.addSequential(DriveStraight(robot))
        self.addSequential(OpenGrabba(robot)) #drops first and second totes on third tote
        self.addSequential(SetLiftSetpoint(robot, -2))
        self.addSequential(LiftGoToLevel(robot))
        self.addSequential(CloseGrabba(robot)) #grabs third tote
        self.addSequential(DriveStraight(robot)) #drives around for a bit

    self.drive.setSafetyEnabled(False)
    