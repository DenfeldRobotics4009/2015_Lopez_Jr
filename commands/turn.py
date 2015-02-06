__author__ = 'auxiliary-character'
from wpilib.command import Command
import wpilib
import math

class Turn(Command):
    def __init__(self, robot, angle):
        super().__init__()
        self.robot = robot
        self.controller = wpilib.PIDController(.05, 0, 0, self.returnPIDInput, self.usePIDOutput)
        self.controller.setSetpoint(robot.drivetrain.gyro.getYaw()+angle)
        self.controller.setAbsoluteTolerance(2)
        self.requires(self.robot.drivetrain)

    def initialize(self):
        self.controller.enable()

    def isFinished(self):
        return self.controller.onTarget()

    def end(self):
        self.controller.disable()
        self.robot.drivetrain.driveManual(0,0,0)

    def interupted(self):
        self.end()

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
        self.robot.drivetrain.driveManual(0, 0, output)
