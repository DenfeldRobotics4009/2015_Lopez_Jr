__author__="nikolojedison"

from wpilib.command import CommandGroup

from .grab_tote import GrabTote
from .lift_go_to_level import LiftGoToLevel
from .open_claw import OpenClaw
from .shaker import Shaker
from wpilib.command import WaitCommand
from .drive_straight import DriveStraight

class ToteLoader(CommandGroup):
    """A command that opens the arms, lowers the lift one tote level, grabs a tote, and raises the lift 1.1 levels."""
    def __init__(self, robot):
        super().__init__()
        loader_generator = [
                LiftGoToLevel(robot, 7),
                OpenClaw(robot),
                LiftGoToLevel(robot, 2),
                DriveStraight(robot, .5, 0, .5),
                GrabTote(robot),
                DriveStraight(robot, -.5, 0, .5),
                GrabTote(robot),
                LiftGoToLevel(robot, 8),
                ]
        for i in loader_generator: self.addSequential(i)
