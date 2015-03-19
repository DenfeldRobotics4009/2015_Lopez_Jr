__author__ = 'nikolojedison'

from wpilib.command import CommandGroup

#Woo, commands
from commands.setpoint_commands.close_claw import CloseClaw
from commands.semiauto_commands.drive_straight import DriveStraight
from commands.setpoint_commands.lift_go_to_level import LiftGoToLevel
from commands.manual_commands.mecanum_drive_with_joystick import MecanumDriveWithJoystick
from commands.setpoint_commands.open_claw import OpenClaw
from commands.set_claw_setpoint import SetClawSetpoint
from commands.set_lift_setpoint import SetLiftSetpoint
from commands.set_mast_setpoint import SetMastSetpoint
from commands.setpoint_commands.grab_tote import GrabTote
from commands.semiauto_commands.turn import Turn
from commands.setpoint_commands.lift_stuff import LiftStuff

class ThreeToteAutonomous(CommandGroup):
    #Should really put some setpoints in. Ehhhhhhh...
    def __init__(self, robot):
        super().__init__()
        self.auton_generator = [
            DriveStraight(robot, 0, -1, timeout=.25),
            Turn(robot, -30),
            DriveStraight(robot, -1, 0, timeout=.1),
            DriveStraight(robot, 0, -1, timeout=.1),
            GrabTote(robot),
            LiftStuff(robot, 1, 1.5),
            GrabTote(robot),
            ]
#            DriveStraight(robot, 0, -.75, timeout=.5),
 #           Turn(robot, 90),
  #          DriveStraight(robot, 0, -.75, timeout=.5),
   #         Turn(robot, -90),
    #        DriveStraight(robot, 0, -.75, timeout=.5),
     #       Turn(robot, 90),
      #      DriveStraight(robot, 0, -.75, timeout=.5),
       #     Turn(robot, -90),
        #    DriveStraight(robot, 0, -.75, timeout=.25),
         #   OpenClaw(robot), #drops first tote on second tote
          #  LiftStuff(robot, -.75, 2),
           # GrabTote(robot),
            #LiftStuff(robot, .75, 2),
#            Turn(robot, 90),
 #           DriveStraight(robot, 0, -.75, timeout=.5),
  #          Turn(robot, -90),
   #         DriveStraight(robot, 0, -.75, timeout=.5),
    #        Turn(robot, 90),
     #       DriveStraight(robot, 0, -.75, timeout=.5),
      #      Turn(robot, -90),
       #     DriveStraight(robot, 0, -.75, timeout=.25),
        #    OpenClaw(robot) #drops 1st and 2nd totes on 3rd tote
         #   LiftStuff(robot, -.75, 2),
          #  GrabTote(robot),
           # LiftStuff(robot, -.75, 2),
            #Turn(robot, 90),
#            DriveStraight(robot, 0, .75, timeout=.5)] #drives around for a bit

        for i in self.auton_generator: self.addSequential(i)

    def cancel(self):
        for i in self.auton_generator: i._cancel()
        super().cancel()
