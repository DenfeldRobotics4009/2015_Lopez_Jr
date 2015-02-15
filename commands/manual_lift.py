from wpilib.command import Command
from drive_control import dead_zone

class ManualLift(Command):
    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        self.requires(self.robot.lift)

    def execute(self):
        self.robot.lift.manualSet(dead_zone(self.robot.oi.getJoystickRight().getY(self), .25))

    def isFinished(self):
        return False

    def cancel(self):
        self.robot.lift.manualSet(0)
        super().cancel()
