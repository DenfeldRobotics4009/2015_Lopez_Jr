__author__ = 'nikolojedison'
from wpilib.command import Command

class LiftLift(Command):
    kTopSetpoint = .9
    def __init__(self, robot): 
        super.__init__(robot, kTopSetpoint)
        
    def isFinished():
        super.isFinished()
    
