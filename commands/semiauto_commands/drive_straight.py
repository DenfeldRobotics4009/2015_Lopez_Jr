__author__ = 'auxiliary-character'
from wpilib.command import Command
import wpilib
import math

class DriveStraight(Command):
    """Drives the robot straight using the navX, PIDs, and a bit of math."""
    def __init__(self, robot, x, y, timeout=None):
        super().__init__()
        self.robot = robot
        self.x = x
        self.y = y
        self.controller = wpilib.PIDController(-.05, 0, 0, self.returnPIDInput, self.usePIDOutput)
        self.requires(self.robot.drivetrain)
        self.setTimeout(timeout)

    def initialize(self):
        self.controller.enable()
        self.controller.setSetpoint(self.robot.drivetrain.gyro.getYaw())

    def isFinished(self):
        return self.isTimedOut()

    def end(self):
        self.controller.disable()
        self.robot.drivetrain.driveManual(0,0,0)

    def interrupted(self):
        self.end()

    def _cancel(self):
        self.end()
        super()._cancel()

    def returnPIDInput(self):
        angle = self.robot.drivetrain.gyro.getYaw()
        set_point = self.controller.getSetpoint()

        angle_greater = angle + 360
        angle_lesser = angle - 360

        use_angle = math.fabs(angle-set_point) < math.fabs(angle_greater - set_point)
        use_angle = use_angle and math.fabs(angle-set_point) < math.fabs(angle_lesser - set_point)
        if use_angle:
            return angle
        elif math.fabs(angle_greater-set_point) < math.fabs(angle_lesser - set_point):
            return angle_greater
        else:
            return angle_lesser

    def usePIDOutput(self, output):
        self.robot.drivetrain.driveManual(self.x, self.y, output)
