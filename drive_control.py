__author__ = 'nikolojedison'
import wpilib

def precision_mode(controller_input, button_state):
    """copied from CubertPy, b/c it worked"""
    if button_state:
        return controller_input * 0.5
    else:
        return controller_input

def exponential_scaling(base, exponent):
    if base>0:
        return abs(base)**exponent
    else:
        return -(abs(base)**exponent)

def coach_dead_zone(motor_output, coach_dead_zone):
    """This is the dead zone with Coach's equation. I really doubt I wrote
    this correctly, please double-check before deployment"""
    if motor_output == 0:
        return 0
    elif motor_output > 0:
        return (motor_output**3 + motor_output)/2
    else:
        return (motor_output**3 - motor_output)/2

def inverse_dead_zone(motor_output, dead_zone):
    """This is the inverted dead zone code which is important for Talons."""
    if abs(motor_output) < .00001: #floating point rounding error workaround.
        return 0
    elif motor_output > 0:
        return (motor_output*(1-dead_zone))+dead_zone
    else:
        return (-motor_output*(dead_zone-1))-dead_zone

def dead_zone(controller_input, dead_zone):
    """This is the dead zone code, essential for any 4009 'bot."""
    if controller_input <= dead_zone and controller_input >= -dead_zone:
        return 0
    elif controller_input > 0:
        return ((controller_input-dead_zone)/(1-dead_zone))
    else:
        return ((-controller_input-dead_zone)/(dead_zone-1))

def drive_control(controller_input, button_state):
    return precision_mode(exponential_scaling(dead_zone(controller_input, 0.1),2.3), button_state)

def drive_control_x(controller_input, button_state):
	"""Because we need a larger dead zone for strafing."""
	return precision_mode(exponential_scaling(dead_zone(cotnroller_input, 0.2),2.3), button_state)

class DriveMotor(wpilib.Talon):
    """A motor controller that overcomes static friction."""
    def set(self, speed, syncGroup=0):
        super().set(inverse_dead_zone(speed, .1),syncGroup=syncGroup)
