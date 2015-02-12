__author__ = 'nikolojedison'
#To change this template use Tools | Templates.
#cancel method stops. Derailer is on a 'while held'
from wpilib.command import Command

class DerailerGo(Command):

    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        self.requires(self.robot.derailer)

    def execute(self):
        self.robot.derailer.set(dead_zone(self.robot.oi.getJoystickRight().getThrottle(), .1))

    def isFinished(self):
        return False

    def end(self):
        self.robot.derailer.set(0)

    def interrupted(self):
        self.end()
