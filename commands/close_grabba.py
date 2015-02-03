__author__ = 'nikolojedison'
import .set_grabba_setpoint

class CloseGrabba(SetGrabbaSetpoint):
    kCloseSetpoint = .1
    kStallPoint = 1.1
    def __init__(self, robot):
        super.__init__(robot, kCloseSetpoint)

    def isFinished():
        #Finishes the command if it reaches the setpoint or current draw is above kStallPoint.
        super.isFinished() or self.robot.grabber.current.getVoltage > kStallPoint
