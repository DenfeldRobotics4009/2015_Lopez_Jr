#Note to self - don't EVER disassemble the mast. Doesn't end well.
#.456 - maximum parallel mast
def scale_reletive(v, top, bottom):
    return v*(top-bottom)+bottom

def unscale_reletive(v, top, bottom):
    return (v-bottom)/(top-bottom)

kMastBack = .300 #This is so the lift won't go up when the mast is back - DO NOT CHANGE IN TESTING
kMastBackLimit = .423
kMastForwardLimit = .482
kMastParallel = .456

#claw setpoints - tested 2/12/15, needs retesting
kOpen = .183
kClose = .890 #2/12/15 23.12: .771 2/13/15 16:30: .925 2/15/15 .070
kCan = .384
kTipped = .425 #This is a tipped can.
kTote = .468
kStall = 2 #This is for the current sensor, which I don't think is still onboard the 'bot.

#lift setpoints - untested
kUp = 3908 #This is so the mast won't tilt when the lift is up
kTop = 4009 #was .651
kBottom = 0 # was .050
kDelta = (kTop-kBottom)
kAboveSecond = scale_reletive(0.1564, kTop, kBottom)
kAboveFirst = scale_reletive(0.2176, kTop, kBottom)
#6.3" per rotation
<<<<<<< HEAD
#lift_levels_reletive = [0.0, 0.0925, 0.2566, 0.4173, 0.5779, 0.7385, 0.8992, 1]
#lift_level_setpoints = [scale_reletive(i, kTop, kBottom) for i in lift_levels_reletive]
lift_level_setpoints = [kBottom, 216, 871, 1526, 2181, 2836, 3491, kTop]
lift_step_setpoints = [i-.015 for i in lift_level_setpoints]
=======
lift_levels_reletive = [0.0, 0.0925, 0.2566, 0.4173, 0.5779, 0.7385, 0.8992, 1]
lift_level_setpoints = [scale_reletive(i, kTop, kBottom) for i in lift_levels_reletive]
lift_step_setpoints = [i-111 for i in lift_level_setpoints] #add 111 for the step
lift_drop_setpoints = [i+333 for i in lift_level_setpoints] #subtract 333 for going down 6"
>>>>>>> New setpoints, yay.
