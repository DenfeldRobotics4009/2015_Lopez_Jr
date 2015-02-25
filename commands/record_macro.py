from wpilib.command import Command
import wpilib
import csv

class RecordMacro(Command):
    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        self.setTimeout(15)

    def initialize(self):
        self.f = open("macro.csv", "w")
        fields = ["Drive_X",
                  "Drive_Y",
                  "Drive_Rotation",
                  "Lift",
                  "Mast",
                  "Claw"]
        self.writer = csv.DictWriter(self.f, fieldnames=fields)

    def execute(self):
        self.writer.write({
            "Drive_X": self.robot.drivetrain.x,
            "Drive_Y": self.robot.drivetrain.y,
            "Drive_Rotation": self.robot.drivetrain.rotation,
            "Lift": self.robot.lift.motor.get(),
            "Mast": self.robot.mast.motor.get(),
            "Claw": self.robot.claw.motor.get()})

    def isFinished(self):
        self.isTimedOut()

    def end(self):
        self.f.close()

    def interrupted(self):
        self.end()

    def cancel(self):
        self.end()
        super().cancel()
