__author__ = "auxiliary-character"
from wpilib.command import Command
from wpilib.timer import Timer
import wpilib
import csv

class RecordMacro(Command):
    """This records robot movements and writes them to a .csv file."""
    def __init__(self, robot, name):
        super().__init__()
        self.robot = robot
        self.setTimeout(15)
        self.name = name

    def initialize(self):
        self.initTime = wpilib.Timer.getFPGATimestamp()
        self.f = open("/home/lvuser/py/"+self.name, "w")
        fields = ["Drive_X",
                  "Drive_Y",
                  "Drive_Rotation",
                  "Lift",
                  "Mast",
                  "Claw",
                  "Lock",
                  "Winch",
                  "Time"]
        self.writer = csv.DictWriter(self.f, fieldnames=fields)
        self.writer.writeheader()

    def execute(self):
        self.writer.writerow({
            "Drive_X": self.robot.drivetrain.x,
            "Drive_Y": self.robot.drivetrain.y,
            "Drive_Rotation": self.robot.drivetrain.rotation,
            "Lift": self.robot.lift.motor.get(),
            "Mast": self.robot.mast.motor.get(),
            "Claw": self.robot.claw.motor.get(),
            "Lock": self.robot.lock.spike.get(),
            "Winch": self.robot.winch.motor.get(),
            "Time": wpilib.Timer.getFPGATimestamp() - self.initTime})

    def isFinished(self):
        return self.isTimedOut()

    def end(self):
        self.f.close()

    def interrupted(self):
        self.end()

    def cancel(self):
        self.end()
        super().cancel()
