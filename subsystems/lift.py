__author__ = 'nikolojedison'
import wpilib
from wpilib.command import Command
from wpilib.command import PIDSubsystem
from wpilib.buttons import Trigger
from commands.manual_lift import ManualLift
import subsystems
import setpoints

class ResetEncoder(Command):
    def __init__(self, robot, lift):
        super().__init__()
        self.robot = robot
        self.lift = lift
    def execute(self):
        self.lift.reset()
    def isFinished(self):
        return True

class EncoderLimitTrigger(Trigger):
    def __init__(self, robot, lift):
        super().__init__()
        self.robot = robot
        self.lift = lift
    def get(self):
        return self.lift.limit_down.get()

class Lift(PIDSubsystem):

    def __init__(self, robot):
        super().__init__(.05, 0, 0)
        self.robot = robot
        self.limit_up = wpilib.DigitalInput(7)
        self.limit_down = wpilib.DigitalInput(6)
        self.lift_encoder = wpilib.Encoder(0, 1)
        self.motor = wpilib.CANTalon(0)
        self.setAbsoluteTolerance(8)
        self.trigger = EncoderLimitTrigger(robot, self)
        self.trigger.whenActive(ResetEncoder(robot, self))

    def initDefaultCommand(self):
        self.setDefaultCommand(ManualLift(self.robot))

    def manualSet(self, output):
        position = self.lift_encoder.get()
        top_limit = self.limit_up.get()
        bottom_limit = self.limit_down.get()
        if bottom_limit and output < 0:
            self.motor.set(0)
        elif top_limit and output > 0:
            self.motor.set(0)
        else:
            if output < 0:
                self.motor.set(output*.75)
            else:
                self.motor.set(output*1)

    def reset(self):
        self.lift_encoder.reset()

    def log(self):
        wpilib.SmartDashboard.putNumber("Elevator Pot", self.lift_encoder.get()) #publishes to the Dash
        wpilib.SmartDashboard.putBoolean("Top Limit", self.limit_up.get())
        wpilib.SmartDashboard.putBoolean("Bottom Limit", self.limit_down.get())

    def returnPIDInput(self):
        return self.lift_encoder.get()

    def usePIDOutput(self, output):
        if output > 1:
            output = 1
        elif output < -1:
            ouput = -1
        self.manualSet(output*1)

    def isUp(self):
        """If the lift is all the way up..."""
        self.lift_encoder.get() > setpoints.kUp
