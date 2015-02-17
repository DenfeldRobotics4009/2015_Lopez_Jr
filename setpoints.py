#Note to self - don't EVER disassemble the mast. Doesn't end well.
#.456 - maximum parallel mast
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
Tote=.104
kUp = .189 #This is so the mast won't tilt when the lift is up
kTop = .105 #was .651
kBottom = .785 # was .050
kDelta = (kTop-kBottom)
#diff of .066
lift_level_setpoints = [kBottom, .732, .627, .510, .398, .286, .179, .555, .465]
lift_step_setpoints = [i-.015 for i in lift_level_setpoints]
