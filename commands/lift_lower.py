__author__ = 'nikolojedison'
from wpilib.command import Command

class LiftLower(Command):
    kBottomSetpoint = -.9
    
    def __init__(self, robot):
        super.__init__(robot, kBottomSetpoint)
        
    def isFinished():
        super.isFinished
      
    