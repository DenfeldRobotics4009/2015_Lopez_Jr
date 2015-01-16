__author__ = 'nikolojedison'
#Various auton utilities.
class Auto(object):
    def __init__(self, robot):
        self.robot = robot

    def forward(sec):
        """drives robot forward for sec seconds... needs to be tested"""
        self.robot.drive.mecanumDrive_Cartesian(0, .5, 0, 0)
        wpilib.Timer.delay(sec)
        self.robot.drive.mecanumDrive_Cartesian(0, 0, 0, 0)

    def tote_grabba():
        """Sets the window motor to half for .5 of a sec to grab the tote."""
        self.robot.window_motor.set(.5)
        wpilib.Timer.delay(.5)
        self.robot.window_motor.set(0)

    def tote_releasa():
        """Releases tote by doing the reverse of tote_grabba"""
        tote_lower(.05)
        self.robot.window_motor.set(-.5)
        wpilib.Timer.delay(.5)
        self.robot.window_motor.set(0)

    def tote_lift(sec):
        self.robot.aux_left.set(.5)
        self.robot.aux_right.set(.5)
        wpilib.Timer.delay(sec)
        self.robot.aux_left.set(0)
        self.robot.aux_right.set(0)

    def tote_lower(sec):
        self.robot.aux_left.set(-.5)
        self.robot.aux_right.set(-.5)
        wpilib.Timer.delay(sec)
        self.robot.aux_left.set(0)
        self.robot.aux_right.set(0)

    def can_slappa():
        """Slappa da can, mon."""
        #do some funky driving here.
