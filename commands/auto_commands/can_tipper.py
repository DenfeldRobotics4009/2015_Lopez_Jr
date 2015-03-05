__author__= 'auxiliary-character'
from wpilib.command import CommandGroup
import wpilib
import math

class CanTipper(CommandGroup):
    """Tippa da can, man. Needs tweaking."""
    def __init__(self, robot):
        super().__init__()
        tipper_generator = [ #need to figure out directions
            Turn(robot, 45),
            DriveStraight(robot, 0, 1, timeout = .1),
            Turn(robot, 90),
            DriveStraight(robot, 0, .5, timeout=.1),
            Turn(robot, -45)]

        [self.addSequential(i) for i in tipper_generator]

        #turn 45 deg
        #go forward x
        #turn 90 deg
        #go forward x
        #turn -45 deg
