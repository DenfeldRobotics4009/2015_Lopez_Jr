__author__ = "auxiliary-character"
from wpilib.command import Command
import csv

class PlayMacro(Command):
    """This plays macro movements from the .csv file."""
    def __init__(self, robot, name):
        super().__init__()
        self.robot = robot
        self.requires(robot.drivetrain)
        self.requires(robot.lift)
        self.requires(robot.claw)
        self.requires(robot.mast)
        self.name = name
        self.done_yet = False

    def initialize(self):
        try:
            self.f = open("/home/lvuser/py/"+self.name)
            self.reader_iterator = iter(csv.DictReader(self.f))
        except FileNotFoundError:
            self.reader_iterator = iter([])
        self.setTimeout(15)

    def execute(self):
        try:
            line = next(self.reader_iterator)
            self.robot.drivetrain.driveManual(float(line["Drive_X"]),
                                              float(line["Drive_Y"]),
                                              float(line["Drive_Rotation"]))
            self.robot.lift.manualSet(float(line["Lift"]))
            self.robot.mast.manualSet(float(line["Mast"]))
            self.robot.claw.manualSet(float(line["Claw"]))
        except StopIteration:
            self.done_yet = True

    def isFinished(self):
        return self.isTimedOut() or self.done_yet

    def end(self):
        self.robot.drivetrain.driveManual(0,0,0)
        self.robot.lift.manualSet(0)
        self.robot.mast.manualSet(0)
        self.robot.claw.manualSet(0)
        if hasattr(self, "f"):
            self.f.close()

    def interrupted(self):
        self.end()

    def cancel(self):
        self.end()
        super().cancel()
