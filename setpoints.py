__author__ = "nikolojedison, auxiliary-character"
#Note to self - don't EVER disassemble the mast when time is of the essence. Doesn't end well.

def scale_reletive(v, top, bottom):
    return v*(top-bottom)+bottom

def unscale_reletive(v, top, bottom):
    return (v-bottom)/(top-bottom)

kMastBack = .423 #This is so the lift won't go up when the mast is back - DO NOT CHANGE IN TESTING
kMastBackLimit = .328
kMastForwardLimit = .482
kMastParallel = .459

#claw setpoints - tested in the heat of battle at the LSR
kOpen = .89
kClose = .185 #2/12/15 23.12: .771 2/13/15 16:30: .925 2/15/15 .070
kCan = .384 #need to update these.
kTipped = .425 #This is a tipped can. Needs update
kTote = .591 #was .468 as of 16:40
kStall = 2 #This is for the current sensor, which I don't think is still onboard the 'bot.
kSpecialTote = 0 #needs update
kSpecialCan = 0 #needs update

#lift setpoints
kUp = 3908 #This is so the mast won't tilt when the lift is up - needed to pass inspection.
kTop = 4009 #IT'S A SIGN. 4009 IS ON TOP.
kBottom = 0 #Coincidentally, this is what the encoder resets to.
kAboveSecond = scale_reletive(0.1564, kTop, kBottom)
kAboveFirst = scale_reletive(0.2176, kTop, kBottom)
#_________________________
#6.3" per encoder rotation
#-------------------------
#lift_levels_reletive = [0.0, 0.0925, 0.2566, 0.4173, 0.5779, 0.7385, 0.8992, 1]
#lift_level_setpoints = [scale_reletive(i, kTop, kBottom) for i in lift_levels_reletive]
lift_level_setpoints = [kBottom, 216, 871, 1526, 2181, 2836, 3491, kTop]
lift_step_setpoints = [i-111 for i in lift_level_setpoints] #add 111 for the step
lift_drop_setpoints = [i+333 for i in lift_level_setpoints] #subtract 333 for going down 6"
