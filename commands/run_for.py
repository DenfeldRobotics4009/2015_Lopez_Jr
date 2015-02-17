from wpilib.command import Command

class RunFor(Command):
    def __init__(self, robot, command, timeout):
        super().__init__()
        self.robot = robot
        self.command = command
        self.setTimeout(timeout)

    def isFinished(self):
        return self.isTimedOut()

    def execute(self):
        self.command.start()

    def end(self):
        self.command.end()

    def interupted(self):
        self.command.interupted()
        self.end()

    def cancel(self):
        self.command.cancel()
        self.end()
        super().cancel()
