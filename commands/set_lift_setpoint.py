__author__ = 'nikolojedison'
class SetLiftSetpoint(Command):

    def __init__(self, robot, setpoint):
        super().__init__()
        self.robot = robot
        
        self.setpoint = setpoint
        self.requires(self.robot.lift)

    def initialize(self):
        self.robot.lift.enable()
        self.robot.lift.setSetpoint(self.setpoint)

    def execute(self):
        """Called repeatedly"""

    def isFinished(self):
        return self.robot.lift.onTarget() #Stay on target...

    def end(self):
        """Called once after isFinisherd returns true"""

    def interrupted(self):
        """Called when another thing which requires one or more of the same subsyses is 
        scheduled to run"""