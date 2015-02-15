from wpilib.command import Command
from drive_control import dead_zone
import setpoints

class ManualClaw(Command):
    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        self.requires(self.robot.claw)

    def execute(self):
        self.robot.claw.manualSet(dead_zone(self.robot.oi.getJoystickRight().getX(), .75))

    def isFinished(self):
        return self.robot.claw.current.getVoltage() > setpoints.kStall

    def cancel(self):
        self.robot.claw.manualSet(0)
        super().cancel()
