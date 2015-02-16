__author__ = 'nikolojedison'
#***************************
#*|\    | | |  /   /  /   |*
#*| \   | | | /      /    |*
#*|  \  | | |/      /     |*
#*|   \ | | |\      ---/  |*
#*|    \| | | \       /   |*
#*|     | | |  \     /    |*
#*|     | | |   \   /     |*
#***************************
#(ascii art, pay no mind.)
#2/12 21:30 - a little tired due to last night, but still going. Waiting on robot.
#2/13 17:53 - waiting on robot, again. Things are working fine in programming though.
#2/13 22:00 - working on setpoints, slowly but surely.
#2/14 13:40 - waiting on more things.
#2/14 23:30 - got the mapping done on the joysticks - waiting on auton testing and a gamepad for presets
#2/15 21:05 - post-ICC. This'll prove interesting.
#2/16
import wpilib
from networktables import NetworkTable
from wpilib.buttons import JoystickButton
from commands.open_claw import OpenClaw
from commands.close_claw import CloseClaw
from commands.center_claw import CenterClaw
from commands.manual_claw import ManualClaw
from commands.manual_lift import ManualLift
from commands.manual_mast import ManualMast
from commands.mast_back import MastBack
from commands.mast_forward import MastForward
from commands.grab_tote import GrabTote
from commands.grab_can import GrabCan
from commands.turn import Turn
from commands.lift_stuff import LiftStuff
from commands.shaker import Shaker
from commands.mast_button import MastButton
from commands.tote_loader import ToteLoader
from pov_button import POVButton
from commands.drive_straight import DriveStraight

class OI:
    """OI! Put yo button maps hea!"""
    def __init__(self, robot):
        """Warning: Metric tonnes of code here. May need to be tidied up a wee bit."""

        self.stick_left = wpilib.Joystick(0)
        self.stick_right = wpilib.Joystick(1)
        self.pad = wpilib.Joystick(2)
        self.smart_dashboard = NetworkTable.getTable("SmartDashboard")

        #Buttons? Aw, man, I love buttons! *bleep bloop*
        #
        # Create some buttons on the left stick (which is really not, but I don't wanna disturb the preexisting code).
        left_trigger = JoystickButton(self.stick_left, 1)
        left_thumb = JoystickButton(self.stick_left, 2)
        left_three = JoystickButton(self.stick_left, 3)
        left_four = JoystickButton(self.stick_left, 4)
        left_five = JoystickButton(self.stick_left, 5)
        left_six = JoystickButton(self.stick_left, 6)
        left_seven = JoystickButton(self.stick_left, 7)
        left_eight = JoystickButton(self.stick_left, 8)
        left_nine = JoystickButton(self.stick_left, 9)
        left_ten = JoystickButton(self.stick_left, 10)
        left_eleven = JoystickButton(self.stick_left, 11)
        left_twelve = JoystickButton(self.stick_left, 12)
        #Create some POV stuff on the left stick, based on angles and the hat switch
        left_north = POVButton(self.stick_left, 0)
        left_northeast = POVButton(self.stick_left, 45)
        left_east = POVButton(self.stick_left, 90)
        left_southeast = POVButton(self.stick_left, 135)
        left_south = POVButton(self.stick_left, 180)
        left_southwest = POVButton(self.stick_left, 225)
        left_west = POVButton(self.stick_left, 270)
        left_northwest = POVButton(self.stick_left, 315)

        #Create some buttons on the ambi stick, see line 48 starting col 49 (Logitech Attack 3)
        right_north = POVButton(self.stick_right, 0)
        right_south = POVButton(self.stick_right, 180)
        right_trigger = JoystickButton(self.stick_right, 1)
        right_thumb = JoystickButton(self.stick_right, 2)
        right_three = JoystickButton(self.stick_right, 3)
        right_four = JoystickButton(self.stick_right, 4)
        right_five = JoystickButton(self.stick_right, 5)
        right_six = JoystickButton(self.stick_right, 6)
        right_seven = JoystickButton(self.stick_right, 7)
        right_eight = JoystickButton(self.stick_right, 8)
        right_nine = JoystickButton(self.stick_right, 9)
        right_ten = JoystickButton(self.stick_right, 10)
        right_eleven = JoystickButton(self.stick_right, 11)

        #25 buttons of stuff on the wall, 25 buttons 'n stuff...
        pad_one = JoystickButton(self.pad, 1)
        pad_two = JoystickButton(self.pad, 2)
        pad_three = JoystickButton(self.pad, 3)
        pad_four = JoystickButton(self.pad, 4)
        pad_five = JoystickButton(self.pad, 5)
        pad_six = JoystickButton(self.pad, 6)
        pad_seven = JoystickButton(self.pad, 7)
        pad_eight = JoystickButton(self.pad, 8)
        pad_nine = JoystickButton(self.pad, 9)
        pad_ten = JoystickButton(self.pad, 10)
        pad_eleven = JoystickButton(self.pad, 11)
        pad_twelve = JoystickButton(self.pad, 12)
        pad_thirteen = JoystickButton(self.pad, 13)
        pad_fourteen = JoystickButton(self.pad, 14)
        pad_fifteen = JoystickButton(self.pad, 15)
        pad_sixteen = JoystickButton(self.pad, 16)
        pad_seventeen = JoystickButton(self.pad, 17)
        pad_eighteen = JoystickButton(self.pad, 18)
        pad_nineteen = JoystickButton(self.pad, 19)
        pad_twenty = JoystickButton(self.pad, 20)
        pad_twentyone = JoystickButton(self.pad, 21)
        pad_twentytwo = JoystickButton(self.pad, 22)
        pad_twentythree = JoystickButton(self.pad, 23)
        pad_twentyfour = JoystickButton(self.pad, 24)
        pad_twentyfive = JoystickButton(self.pad, 25)

        # Connect buttons & commands
        #Right: 4 is tote level 5 is bottomed out
        left_south.whenPressed(DriveStraight(robot, 0, .25, timeout = .25))
        left_north.whenPressed(DriveStraight(robot, 0, -.25, timeout = .25))
        left_east.whenPressed(DriveStraight(robot, .25, 0, timeout = .35))
        left_west.whenPressed(DriveStraight(robot, -.25, 0, timeout = .35))
        right_north.whileHeld(MastButton(robot, .38))
        right_south.whileHeld(MastButton(robot, -.38))
        left_thumb.whileHeld(Shaker(robot)) #like a Polaroid picture
        left_five.whenPressed(ToteLoader(robot))
        left_six.whenPressed(LiftStuff(robot, 1, .1))
        left_four.whenPressed(LiftStuff(robot, -1, .1))
        #right_trigger.whenPressed() #does some cool 2" lifting and stuff

    def getJoystickLeft(self):
        """This is the left joystick."""
        return self.stick_left

    def getJoystickRight(self):
        """This is the right joystick."""
        return self.stick_right

    def getPad(self):
        """This is the pad."""
        return self.pad
