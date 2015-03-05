__author__ = 'nikolojedison'

from wpilib.command import Command

class SetClawSetpoint(Command):

    def __init__(self, robot, setpoint):
        super().__init__()
        self.robot = robot
        self.setTimeout(5)
        self.setpoint = setpoint
        self.requires(self.robot.claw)

    def initialize(self):
        self.robot.claw.enable()
        self.robot.claw.setSetpoint(self.setpoint)

    def execute(self):
        """Called repeatedly"""

    def isFinished(self):
        return self.robot.claw.onTarget() or self.isTimedOut() #Stay on target...

    def end(self):
        """Called once after isFinisherd returns true"""
        self.robot.claw.disable()

    def interrupted(self):
        """Called when another thing which requires one or more of the same subsyses is
        scheduled to run"""
        self.end()
