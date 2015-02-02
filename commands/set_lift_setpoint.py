__author__ = 'nikolojedison'

from wpilib.command import Command

class SetLiftSetpoint(Command):

    def __init__(self, robot, setpoint):
        super().__init__()
        self.robot = robot
        
        self.setpoint = setpoint
        self.requires(self.robot.lift)

    def initialize(self):
        self.robot.lift.enable()
        self.robot.lift.setSetpoint(self.setpoint)

    def isFinished(self):
        return self.robot.lift.onTarget() #Stay on target...
    