__author__="nikolojedison"

from wplilib.command import CommandGroup

from .grab_tote import GrabTote
from .lift_stuff import LiftStuff
from .open_claw import OpenClaw

class ToteLoader(CommandGroup):
    """A command that takes the bottom tote, lifts it, waits a bit, then drops the tote and grabs the bottom tote."""
    def __init__(self, robot):
        super().__init__()
        loader_generator = [
                GrabTote(robot),
                LiftStuff(robot, 1, 2.5),
                #waits, consult Austin
                LiftStuff(robot, -1, .5),
                OpenClaw(robot),
                LiftStuff(robot, -1, 1.9)]
        for i in loader_generator: self.addSequential(i)
