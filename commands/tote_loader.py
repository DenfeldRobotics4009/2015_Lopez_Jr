__author__="nikolojedison"

from wpilib.command import CommandGroup

from .grab_tote import GrabTote
from .lift_stuff import LiftStuff
from .open_claw import OpenClaw
from wpilib.command import WaitCommand

class ToteLoader(CommandGroup):
    """A command that opens the arms, lowers the lift one tote level, grabs a tote, and raises the lift 1.1 levels."""
    def __init__(self, robot):
        super().__init__()
        loader_generator = [
                OpenClaw(robot),
                LiftStuff(robot, -1, 2),
                GrabTote(robot),
                LiftStuff(robot, 1, 2.25),
        for i in loader_generator: self.addSequential(i)
