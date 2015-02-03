__author__ = 'nikolojedison'
import wpilib

from wpilib import SmartDashboard



class OI:

    def __init__(self, robot):

        self.stick_left = wpilib.Joystick(0)
        self.stick_right = wpilib.Joystick(1)
        self.smart_dashboard = NetworkTable.getTable("SmartDashboard")


        # Create some buttons on the left stick
        left_trigger = JoystickButton(self.stick_left, 0)
        left_thumb = JoystickButton(self.stick_left, 1)
        left_three = JoystickButton(self.stick_left, 2)
        left_four = JoystickButton(self.stick_left, 3)
        left_five = JoystickButton(self.stick_left, 4)
        left_six = JoystickButton(self.stick_left, 5)
        left_seven = JoystickButton(self.stick_left, 6)
        left_eight = JoystickButton(self.stick_left, 7)
        left_nine = JoystickButton(self.stick_left, 8)
        left_ten = JoystickButton(self.stick_left, 9)
        left_eleven = JoystickButton(self.stick_left, 10)
        left_twelve = JoystickButton(self.stick_left, 11)

        #Create some buttons on the right stick
        right_trigger = JoystickButton(self.stick_right, 0)
        right_thumb = JoystickButton(self.stick_right, 1)
        right_three = JoystickButton(self.stick_right, 2)
        right_four = JoystickButton(self.stick_right, 3)
        right_five = JoystickButton(self.stick_right, 4)
        right_six = JoystickButton(self.stick_right, 5)
        right_seven = JoystickButton(self.stick_right, 6)
        right_eight = JoystickButton(self.stick_right, 7)
        right_nine = JoystickButton(self.stick_right, 8)
        right_ten = JoystickButton(self.stick_right, 9)
        right_eleven = JoystickButton(self.stick_right, 10)
        right_twelve = JoystickButtonself.stick_right, 11)

        # Connect the buttons to commands
        l2.whenPressed(Autonomous(robot))

    def getJoystickLeft(self):
        return self.stick_left

    def getJoystickRight(self):
        return self.stick_right
