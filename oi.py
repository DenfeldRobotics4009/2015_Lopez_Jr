__author__ = 'nikolojedison'
#**************************
#|\    | | |  / /    /   |*
#| \   | | | /      /    |*
#|  \  | | |/      /     |*
#|   \ | | |\      ---/  |*
#|    \| | | \       /   |*
#|     | | |  \     /     *
#|     | | |   \   /     |*
#**************************
#(ascii art OP. Pls nerf.)
import wpilib
from networktables import NetworkTable
from wpilib.buttons import JoystickButton
#from commands.autonomous import Autonomous
from commands.open_claw import OpenClaw
from commands.close_claw import CloseClaw
from commands.center_claw import CenterClaw
from commands.manual_claw import ManualClaw
from commands.manual_lift import ManualLift
from commands.manual_mast import ManualMast
from commands.mast_back import MastBack
from commands.mast_forward import MastForward
from commands.grab_tote import GrabTote
from pov_button import POVButton
from commands.drive_straight import DriveStraight

class OI:
    """OI! Put yo button maps hea!"""
    def __init__(self, robot):
        """Warning: Metric tonnes of code here. May need to be tidied up a wee bit."""

        self.stick_left = wpilib.Joystick(0)
        self.stick_right = wpilib.Joystick(1)
        self.smart_dashboard = NetworkTable.getTable("SmartDashboard")


        # Create some buttons on the left stick
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
        #Create some POV stuff on the left stick, based on the cardinal directions and the hat switch - may end up being degrees,
        #with north = 0, east = 90, south = 180, west 270
        left_north = POVButton(self.stick_left, 0)
        left_northeast = POVButton(self.stick_left, 1)
        left_east = POVButton(self.stick_left, 2)
        left_southeast = POVButton(self.stick_left, 3)
        left_south = POVButton(self.stick_left, 4)
        left_southwest = POVButton(self.stick_left, 5)
        left_west = POVButton(self.stick_left, 6)
        left_northwest = POVButton(self.stick_left, 7)

        #Create some buttons on the right stick
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
        right_twelve = JoystickButton(self.stick_right, 12)
        #Create some POV stuff on the right stick, see lines 39-40 for explanation
        right_north = POVButton(self.stick_right, 0)
        right_northeast = POVButton(self.stick_right, 1)
        right_east = POVButton(self.stick_right, 2)
        right_southeast = POVButton(self.stick_right, 3)
        right_south = POVButton(self.stick_right, 4)
        right_southwest = POVButton(self.stick_right, 5)
        right_west = POVButton(self.stick_right, 6)
        right_northwest = POVButton(self.stick_right, 7)

        # Connect the buttons to commands, this code is an example of how to do it.
        #left_thumb.whenPressed(Autonomous(robot))
        right_thumb.whenPressed(GrabTote(robot))
        right_three.whenPressed(CloseClaw(robot))
        right_four.whenPressed(MastBack(robot))
        right_five.whenPressed(OpenClaw(robot))
        right_six.whenPressed(MastForward(robot))
        right_eight.whileHeld(ManualLift(robot))
        right_nine.whileHeld(ManualMast(robot))
        right_eleven.whileHeld(ManualClaw(robot))
        left_thumb.whenPressed(DriveStraight(robot, 0, .15, timeout = .25))
        #right_trigger.whenPressed() #does some cool 2" lifting and stuff
        #right_thumb.whenPressed() #grabs one tote width

    def getJoystickLeft(self):
        return self.stick_left

    def getJoystickRight(self):
        return self.stick_right
