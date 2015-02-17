__author__="nikolojedison"

from wpilib.command import CommandGroup

from .grab_tote import GrabTote
from .lift_go_to_level import LiftGoToLevel
from .open_claw import OpenClaw
from wpilib.command import WaitCommand

class ToteLoader(CommandGroup):
    """A command that opens the arms, lowers the lift one tote level, grabs a tote, and raises the lift 1.1 levels."""
    def __init__(self, robot):
        super().__init__()
        loader_generator = [
                LiftGoToLevel(robot, 3),
                OpenClaw(robot),
                LiftGoToLevel(robot, 2),
                GrabTote(robot),
                LiftGoToLevel(robot, 4),
                ]
        for i in loader_generator: self.addSequential(i)
