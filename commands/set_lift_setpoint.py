__author__ = 'nikolojedison'

from wpilib.command import Command

class SetLiftSetpoint(Command):

    def __init__(self, robot, setpoint):
        super().__init__()
        self.robot = robot
        self.setTimeout(5)

        self.setpoint = setpoint
        self.requires(self.robot.lift)

    def initialize(self):
        self.robot.lift.enable()
        self.robot.lift.setSetpoint(self.setpoint)

    def isFinished(self):
        return self.robot.lift.onTarget() or self.isTimedOut() #Stay on target...

    def end(self):
        self.robot.lift.disable()

    def interupted(self):
        self.end()

    def cancel(self):
        self.end()
        super().cancel()
