from wpilib.command import Command
from drive_control import dead_zone

class ManualGrabba(Command):
    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        self.requires(self.robot.grabber)

    def execute(self):
        self.robot.grabber.manualSet(dead_zone(self.robot.oi.getJoystickLeft().getThrottle(), .1))

    def isFinished(self):
        return False

    def cancel(self):
        self.robot.grabber.manualSet(0)
        super().cancel()
