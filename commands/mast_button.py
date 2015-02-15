from wpilib.command import Command

class MastButton(Command):
    def __init__(self, robot, speed):
        super().__init__()
        self.robot = robot
        self.requires(self.robot.lift)
        self.speed = speed

    def execute(self):
        position = self.mast_pot.get()
        if position < kMastBackLimit:
            self.motor.set(0)
        elif position > kMastForwardLimit:
            self.motor.set(0)
        self.robot.mast.manualSet(self.speed)

    def isFinished(self):
        return False

    def cancel(self):
        self.robot.lift.manualSet(0)
        super().cancel()
