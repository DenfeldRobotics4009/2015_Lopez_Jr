__author__ = 'nikolojedison'

from wpilib.command import CommandGroup

#commands everywhere
from commands.setpoint_commands.grab_tote import GrabTote
from commands.semiauto_commands.drive_straight import DriveStraight
from commands.setpoint_commands.lift_go_to_level import LiftGoToLevel
from commands.manual_commands.mecanum_drive_with_joystick import MecanumDriveWithJoystick
from commands.setpoint_commands.open_claw import OpenClaw
from commands.set_claw_setpoint import SetClawSetpoint
from commands.set_lift_setpoint import SetLiftSetpoint
from commands.set_mast_setpoint import SetMastSetpoint
from commands.semiauto_commands.turn import Turn
from commands.setpoint_commands.lift_stuff import LiftStuff
from commands.setpoint_commands.lift_go_to_level import LiftGoToLevel

class ToteAutonomous(CommandGroup):
    """This is the autonomous where we grab the can and drive off with it."""
    #Clamp, lift up, turn 45 deg left, go forward, drop can
    def __init__(self, robot):
        super().__init__()
        auton_generator = [
            LiftGoToLevel(robot, 2),
            GrabTote(robot), #grabs can
            LiftGoToLevel(robot, 4),
            DriveStraight(robot, 0, -.5, timeout=1),
            Turn(robot, -45),
            DriveStraight(robot, 0, -.5, timeout=2.5),
            LiftGoToLevel(robot, 2),
            OpenClaw(robot), #drops can
            DriveStraight(robot, 0, .5, timeout=.25)]

        #generates the autonomous (reeeeeally cool command, thanks Austin!)
        for i in auton_generator: self.addSequential(i)
