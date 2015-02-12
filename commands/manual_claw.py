from wpilib.command import Command
from drive_control import dead_zone

class ManualClaw(Command):
    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        self.requires(self.robot.claw)

    def execute(self):
        self.robot.claw.manualSet(dead_zone(self.robot.oi.getJoystickRight().getThrottle(), .1))

    def isFinished(self):
        return False

    def cancel(self):
        self.robot.claw.manualSet(0)
        super().cancel()
