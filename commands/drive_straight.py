__author__ = 'auxiliary-character'
import wpilib.command.PIDCommand
class DriveStraight(PIDCommand):
    def __init__(self, robot, x, y, angle, name=None, timeout=None):
        self.robot = robot
        self.x = x
        self.y = y
        self.angle = angle
        self.setSetpoint(angle)
        self.requires(self.robot.drivetrain)
        super.__init__(name,timeout)
    
    def isFinished(self):
        if self.isTimedOut():
            self.robot.drivetrain.driveManual(0,0,0)
    
    def returnPIDInput()
        angle = self.gyro.getYaw()
        