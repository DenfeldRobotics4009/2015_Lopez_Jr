__author__ = "auxiliary-character"
from wpilib.command import Command
import csv

class PlayMacro(Command):
    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        self.requires(robot.drivetrain)
        self.requires(robot.lift)
        self.requires(robot.claw)
        self.requires(robot.mast)
        self.f = open("macro.csv")
        self.reader_iterator = iter(csv.DictReader(self.f))
        self.done_yet = False
        self.setTimeout(15)

    def execute(self):
        try:
            line = next(self.reader_iterator)
            self.robot.drivetrain.driveManual(line["Drive_X"],
                                              line["Drive_Y"],
                                              line["Drive_Rotation"])
            self.robot.lift.setManual(line["Lift"])
            self.robot.mast.setManual(line["Mast"])
            self.robot.claw.setManual(line["Claw"])
        except StopIteration:
            self.done_yet = True

    def isFinished(self):
        return self.isTimedOut() or self.done_yet

    def end(self):
        self.f.close()

    def interrupted(self):
        self.end()

    def cancel(self):
        self.end()
        super().cancel()
