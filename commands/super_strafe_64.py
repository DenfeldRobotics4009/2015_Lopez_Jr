import wpilib
from wpilib.command import Command

class SuperStrafe64(Command):
    """Only for Nintendo 64."""
    def __init__(self, robot, inverted):
        super().__init__()
        self.robot = robot
        self.requires(robot.drivetrain)
        self.setTimeout(.7)
        if inverted:
            self.kInverted = -1
        else:
            self.kInverted = 1

    def execute(self):
        time = self.timeSinceInitialized()
        if time < .5:
            self.robot.drivetrain.driveManual(time * self.kInverted, 0, 0)
        else:
            self.robot.drivetrain.driveManual(-1 * self.kInverted, 0, 0)

    def isFinished(self):
        return self.isTimedOut()

    def end(self):
        self.robot.drivetrain.driveManual(0,0,0)

    def interrupted(self):
        self.end()

    def cancel(self):
        self.end()
        super().cancel()
