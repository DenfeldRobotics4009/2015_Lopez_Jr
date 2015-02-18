#Note to self - don't EVER disassemble the mast. Doesn't end well.
#.456 - maximum parallel mast
def scale_reletive(v, top, bottom):
    return v*(top-bottom)+bottom

kMastBack = .300 #This is so the lift won't go up when the mast is back - DO NOT CHANGE IN TESTING
kMastBackLimit = .311
kMastForwardLimit = .482
kMastParallel = .416

#claw setpoints - tested 2/12/15
kOpen = .183
kClose = .890 #2/12/15 23.12: .771 2/13/15 16:30: .925 2/15/15 .070
kCan = .458
kTote = .537
kStall = 2 #This is for the current sensor.

#lift setpoints - untested
kUp = .189 #This is so the mast won't tilt when the lift is up
kTop = 4009 #was .651
kBottom = 0 # was .050
kDelta = (kTop-kBottom)
kAboveSecond = scale_reletive(0.1564, kTop, kBottom)
kAboveFirst = scale_reletive(0.2176, kTop, kBottom)
#6.3" per rotation
lift_levels_reletive = [-0.0, 0.0779, 0.2323, 0.4044, 0.5691, 0.7338, 0.8911]
lift_level_setpoints = [scale_reletive(i, kTop, kBottom) for i in lift_levels_reletive]
lift_step_setpoints = [i-.015 for i in lift_level_setpoints]
