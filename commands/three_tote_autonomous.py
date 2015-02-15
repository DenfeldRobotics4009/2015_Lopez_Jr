__author__ = 'nikolojedison'
from wpilib.command import CommandGroup

from .close_claw import CloseClaw
from .drive_straight import DriveStraight
from .lift_go_to_level import LiftGoToLevel
from .mecanum_drive_with_joystick import MecanumDriveWithJoystick
from .open_claw import OpenClaw
from .set_claw_setpoint import SetClawSetpoint
from .set_lift_setpoint import SetLiftSetpoint
from .set_mast_setpoint import SetMastSetpoint
from .grab_tote import GrabTote
from .turn import Turn

class ThreeToteAutonomous(CommandGroup):
    #Should really put some setpoints in. Ehhhhhhh...
    def __init__(self, robot):
        super().__init__()
        self.auton_generator = [
            DriveStraight(robot, 0, -.2, timeout=.5),
            GrabTote(robot),
            Turn(robot, 45),
            LiftStuff(robot, .75, 2),
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
            #Turn(robot, 90)
#            DriveStraight(robot, 0, .75, timeout=.5)] #drives around for a bit

        for i in self.auton_generator: self.addSequential(i)

    def cancel(self):
        for i in self.auton_generator: i._cancel()
        super().cancel()
