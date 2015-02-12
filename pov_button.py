from wpilib.buttons import Button

class POVButton(Button):
    """This is the POVButton class, and is critical to the operation of things. Import it into oi.py
    and code like the joystickButtons, but instead of buttons do postitions (clockwise). Be careful
    though - should be used for directional stuff b/c of the way it works."""
    def __init__(self, joystick, pov=0):
        super().__init__()
        self.joystick = joystick
        self.POVNumber = pov

    def get(self):
        return self.joystick.getPOV(pov = self.POVNumber)
