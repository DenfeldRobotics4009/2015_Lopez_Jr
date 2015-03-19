__author__ = "auxiliary-character"
import wpilib
from wpilib.timer import Timer
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
        #self.requires(robot.winch)
        #self.requires(robot.lock)
        self.name = name
        self.done_yet = False

    def initialize(self):
        try:
            if self.robot.isReal():
                self.f = open("/home/lvuser/py/"+self.name)
            else:
                self.f = open(self.name)
            self.reader_iterator = csv.DictReader(self.f)
        except FileNotFoundError:
            self.reader_iterator = []
        self.setTimeout(15)
        start_time = Timer.getFPGATimestamp()
        for line in self.reader_iterator:
            wpilib.Timer.delay(float(line["Time"]) - (Timer.getFPGATimestamp()-start_time))
            self.robot.drivetrain.driveManual(float(line["Drive_X"]),
                                            float(line["Drive_Y"]),
                                            float(line["Drive_Rotation"]))
            self.robot.lift.manualSet(float(line["Lift"]))
            self.robot.mast.manualSet(float(line["Mast"]))
            self.robot.claw.manualSet(float(line["Claw"]))
           # self.robot.lock.spike.set(int(line["Lock"]))
          #  self.robot.winch.manualSet(float(line["Winch"]))
            if self.isTimedOut() or self.done_yet:
                break


    def execute(self):
        pass

    def isFinished(self):
        return True

    def end(self):
        self.robot.drivetrain.driveManual(0,0,0)
        self.robot.lift.manualSet(0)
        self.robot.mast.manualSet(0)
        self.robot.claw.manualSet(0)
        #self.robot.winch.manualSet(0)
        if hasattr(self, "f"):
            self.f.close()

    def interrupted(self):
        self.end()

    def cancel(self):
        self.end()
        super().cancel()
