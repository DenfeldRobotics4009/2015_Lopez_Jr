_author__ = 'nikolojedison'
import wpilib
from wpilib.command import PIDSubsystem
from commands.manual_commands.manual_claw import ManualClaw
import setpoints

class Claw(PIDSubsystem):
    """This is a claw. It does claw things."""

    def __init__(self, robot):
        super().__init__(20, 0, 0)
        self.robot = robot

        self.grabba_pot = wpilib.AnalogPotentiometer(2)
        self.motor = wpilib.Talon(5)
        self.current = wpilib.AnalogInput(3)
        self.setAbsoluteTolerance(.01)

    def initDefaultCommand(self):
        self.setDefaultCommand(ManualClaw(self.robot))

    def log(self):
        wpilib.SmartDashboard.putNumber("Clamp Pot", self.grabba_pot.get()) #publishes to the Dash
        wpilib.SmartDashboard.putNumber("Current Regulator", self.current.getVoltage())

    def manualSet(self, output):
        position = self.grabba_pot.get()
        if position < (setpoints.kClose+.013) and output < 0:
            self.motor.set(0)
        elif position > (setpoints.kOpen-.013) and output > 0:
            self.motor.set(0)
        else:
            self.motor.set(output)

    def returnPIDInput(self):
        return self.grabba_pot.get()

    def usePIDOutput(self, output):
        self.manualSet(output)
