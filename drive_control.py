__author__ = 'nikolojedison'

def precision_mode(controller_input, button_state):
    """copied from CubertPy, b/c it worked"""
    if button_state:
        return controller_input * 0.5
    else:
        return controller_input

def dead_zone(controller_input, dead_zone):
    if controller_input <= dead_zone and controller_input >= -dead_zone:
        return 0
    elif controller_input > 0:
        controller_input = ((controller_input-dead_zone)/(1-dead_zone))
    else:
        controller_input = ((-controller_input-dead_zone)/(dead_zone-1))

def drive_control(controller_input, button_state):
    return precision_mode(dead_zone(controller_input, .1)**3, button_state)
