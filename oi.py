__author__ = 'nikolojedison'

#2/12 21:30 - a little tired due to last night, but still going. Waiting on robot.
#2/13 17:53 - waiting on robot, again. Things are working fine in programming though.
#2/13 22:00 - working on setpoints, slowly but surely.
#2/14 13:40 - waiting on more things.
#2/14 23:30 - got the mapping done on the joysticks - waiting on auton testing and a gamepad for presets
#2/15 21:05 - post-ICC. This'll prove interesting.
#2/16 15:06 - gamepad is finally here, recalculated setpoints. Still deciding on what is going to map where.
#2/17 09:53 - Getting close on implementing the gamepad. Noticed that this is the first dev log with only 3 digits.
#2/17 16:30 - new joysticks, remapping EVERYTHING.
#2/17 19:45 - Potentiometer replaced with an encoder. Broke everything.
#2/19 16:17 - Well, robot is bagged. We'll see how this goes.
#2/26 09:33 - @ LSR, waiting for power to deploy newest code.
#2/26 13:10 - @ LSR, code works. Time to figure out what Auton is.
#2/26 15:26 - @ LSR, inspection passed. Drive team is practicing. Auton may come someday.
#2/26 16:30 - @ LSR, pots have stalled. Trying to figure out what's wrong.
#2/27 09:50 - @ LSR, got the Auton macro working. Queued for our first Quals match.
#2/27 10:44 - @ LSR, MiniMatt the human player was awesome at noodle throwing. Drive team... needs practice.
#2/27 13:07 - @ LSR, done with lunch & waiting for the afternoon match.
#2/27 13:20 - @ LSR, prepping for afternoon match with new attachments & the Principal.
#2/27 16:42 - @ LSR, went from low 40s to 8th in two matches with the first scoring 124 points (yay programmer on the field)
#2/28 09:04 - @ LSR, our first match scored in the 70s. Working on checking wires.
#2/28 09:33 - @ LSR, installing Hall Effect sensor (fully tested). All down to Build now. Also, 4th place.
#2/28 09:38 - @ LSR, nevermind 4th, we're 3rd. Cool.
#2/28 12:50 - @ LSR, was 8th, but now we're the 6th(?) alliance. Lunch break.
#2/28 14:07 - @ LSR, in queue.

#Libraries
import wpilib
from networktables import NetworkTable
from wpilib.buttons import JoystickButton, InternalButton

#Commands
from commands.timed_turn import TimedTurn
from commands.setpoint_commands.lift_go_to_level import LiftGoToLevel
from commands.setpoint_commands.lift_go_to_level_shift import LiftGoToLevelShift
from commands.setpoint_commands.open_claw import OpenClaw
from commands.setpoint_commandsclose_claw import CloseClaw
from commands.setpoint_commands.center_claw import CenterClaw
from commands.manual_commands.manual_claw import ManualClaw
from commands.manual_commands.manual_lift import ManualLift
from commands.setpoint_commands.mast_level import MastLevel
from commands.manual_commands.manual_mast import ManualMast
from commands.setpoint_commands.mast_back import MastBack
from commands.setpoint_commands.mast_forward import MastForward
from commands.setpoint_commands.grab_tote import GrabTote
from commands.setpoint_commands.grab_special_tote import GrabSpecialTote
from commands.setpoint_commands.grab_special_can import GrabSpecialCan
from commands.setpoint_commands.grab_can import GrabCan
from commands.semiauto_commands.turn import Turn
from commands.setpoint_commands.lift_stuff import LiftStuff
from commands.semiauto_commands.shaker import Shaker
from commands.setpoint_commands.mast_button import MastButton
from commands.semiauto_commands.tote_loader import ToteLoader
from commands.semiauto_commands.super_strafe_64 import SuperStrafe64 #Only on Nintendo64.
from commands.semiauto_commands.drive_straight import DriveStraight
from commands.record_macro import RecordMacro
from commands.play_macro import PlayMacro

#Libraries we wrote
from pov_button import POVButton
import setpoints

class KeyButton(InternalButton):
    """This is doing the impossible right here. Don't use w/o the driver station."""
    def __init__(self, table, code):
        super().__init__()
        self.code = code
        def listener(table, key, value, isNew):
            if key=="Keys":
                if self.code in value:
                    self.setPressed(True)
                else:
                    self.setPressed(False)
        table.addTableListener(listener)

class OI:
    """OI! Put yo button maps hea!"""
    def __init__(self, robot):
        """Warning: Metric tonnes of code here. May need to be tidied up a wee bit."""

        self.stick_left = wpilib.Joystick(0)
        self.pad = wpilib.Joystick(1)
        self.smart_dashboard = NetworkTable.getTable("SmartDashboard")

        #Buttons? Aw, man, I love buttons! *bleep bloop*
        #-----------------------------------------------

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

        #Keypad Buttons
        g1 = KeyButton(self.smart_dashboard, 10)
        g2 = KeyButton(self.smart_dashboard, 11)
        g3 = KeyButton(self.smart_dashboard, 12)
        g4 = KeyButton(self.smart_dashboard, 13)
        g5 = KeyButton(self.smart_dashboard, 14)
        g6 = KeyButton(self.smart_dashboard, 15)
        g7 = KeyButton(self.smart_dashboard, 16)
        g8 = KeyButton(self.smart_dashboard, 17)
        g9 = KeyButton(self.smart_dashboard, 18)
        g10 = KeyButton(self.smart_dashboard, 19)
        g11 = KeyButton(self.smart_dashboard, 20)
        g12 = KeyButton(self.smart_dashboard, 21)
        g13 = KeyButton(self.smart_dashboard, 22)
        g14 = KeyButton(self.smart_dashboard, 23)
        g15 = KeyButton(self.smart_dashboard, 24)
        g16 = KeyButton(self.smart_dashboard, 25)
        g17 = KeyButton(self.smart_dashboard, 26)
        g18 = KeyButton(self.smart_dashboard, 27)
        g19 = KeyButton(self.smart_dashboard, 28)
        g20 = KeyButton(self.smart_dashboard, 29)
        g21 = KeyButton(self.smart_dashboard, 30)
        g22 = KeyButton(self.smart_dashboard, 31)
        topshift = KeyButton(self.smart_dashboard, 32)
        bottomshift = KeyButton(self.smart_dashboard, 33)
        extra1 = KeyButton(self.smart_dashboard, 34)
        extra2 = KeyButton(self.smart_dashboard, 35)
        #25 buttons of stuff on the wall, 25 buttons 'n stuff...

        # Connect buttons & commands
        #---------------------------

        #Bump commands
        left_south.whenPressed(DriveStraight(robot, 0, .25, timeout = .25))
        left_north.whenPressed(DriveStraight(robot, 0, -.25, timeout = .25))
        left_east.whenPressed(DriveStraight(robot, .25, 0, timeout = .35))
        left_west.whenPressed(DriveStraight(robot, -.25, 0, timeout = .35))

        #Mast control
        left_five.whileHeld(MastButton(robot, .38))
        left_six.whileHeld(MastButton(robot, -.38))
        left_thumb.whileHeld(Shaker(robot)) #like a Polaroid picture
        left_nine.whenPressed(SuperStrafe64(robot, SuperStrafe64.kLeft))
        left_ten.whenPressed(SuperStrafe64(robot, SuperStrafe64.kRight))
        left_seven.whenPressed(SuperStrafe64(robot, SuperStrafe64.kForward))
        left_eight.whenPressed(SuperStrafe64(robot, SuperStrafe64.kBack))

        #Lift presets
        g1.whenPressed(LiftGoToLevelShift(robot, 1, topshift, bottomshift))
        g2.whenPressed(LiftGoToLevelShift(robot, 2, topshift, bottomshift))
        g3.whenPressed(LiftGoToLevelShift(robot, 3, topshift, bottomshift))
        g4.whenPressed(LiftGoToLevelShift(robot, 4, topshift, bottomshift))
        g5.whenPressed(LiftGoToLevelShift(robot, 5, topshift, bottomshift))
        g6.whenPressed(LiftGoToLevelShift(robot, 6, topshift, bottomshift))
        g7.whenPressed(LiftGoToLevelShift(robot, 7, topshift, bottomshift))
        g8.whenPressed(LiftGoToLevelShift(robot, 0, topshift, bottomshift))

        g9.whenPressed(RecordMacro(robot, "macro_2.csv"))
        g10.whenPressed(PlayMacro(robot, "macro_2.csv"))

        #g12 and g13 are for testing only and NOT for match use!
        g11.whenPressed(RecordMacro(robot, "macro_1.csv"))
        g12.whenPressed(PlayMacro(robot, "macro_1.csv"))

        g13.whenPressed(RecordMacro(robot, "macro.csv"))
        g14.whenPressed(PlayMacro(robot, "macro.csv"))

        g15.whenPressed(RecordMacro(robot, "macro_3.csv"))
        g16.whenPressed(PlayMacro(robot, "macro_3.csv"))

        g17.whenPressed(RecordMacro(robot, "macro_4.csv"))
        g18.whenPressed(PlayMacro(robot, "macro_4.csv"))

        g19.whenPressed(CloseClaw(robot))
        g20.whenPressed(MastBack(robot))
        g21.whenPressed(MastLevel(robot))
        g22.whenPressed(MastForward(robot))
        #top shift - all levels -.015 for platform stacking
        #bottom shift - all levels +.045 for setdown

    def getJoystickLeft(self):
        """This is the driver's joystick, v. fancy."""
        return self.stick_left

    def getPad(self):
        """This is the gamepad's joystick."""
        return self.pad
