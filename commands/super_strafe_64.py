import wpilib
from wpilib.command import Command

class SuperStrafe64(Command):
    """Only for Nintendo 64."""
    kBack = 0
    kForward = 1
    kRight = 2
    kLeft = 3
    def __init__(self, robot, direction):
        super().__init__()
        self.robot = robot
        self.requires(robot.drivetrain)
        self.setTimeout(.7)
        self.direction = direction

    def actuate(self, amount):
        if self.direction == self.kBack:
            self.robot.drivetrain.driveManual(0, amount, amount/5)
        elif self.direction == self.kForward:
            self.robot.drivetrain.driveManual(0, -amount, amount/5)
        elif self.direction == self.kRight:
            self.robot.drivetrain.driveManual(amount, 0, 0)
        elif self.direction == self.kLeft:
            self.robot.drivetrain.driveManual(-amount, 0, 0)

    def execute(self):
        time = self.timeSinceInitialized()
        if time < .5:
            self.actuate(time)
        else:
            self.actuate(-1)

    def isFinished(self):
        return self.isTimedOut()

    def end(self):
        self.actuate(0)

    def interrupted(self):
        self.end()

    def cancel(self):
        self.end()
        super().cancel()
