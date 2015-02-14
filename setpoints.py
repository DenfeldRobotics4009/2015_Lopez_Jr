#mast setpoints - 2/13/15
kMastBack = .3 #This is so the lift won't go up when the mast is back
kMastBackLimit = .289
kMastForwardLimit = .433
kMastParallel = .416

#claw setpoints - tested 2/12/15
kOpen = .200
kClose = .925 #2/12/15 23.12: .771 2/13/15 16:30: .925
kCan = .375
kTote = .505
kStall = 2 #This is for the current sensor.

#lift setpoints - untested
kUp = .640 #This is so the mast won't tilt when the lift is up
kTop = .64 #was .651
kBottom = .047
lift_level_setpoints = [kBottom, .075, .179, .264, .362, .466, .568, kTop]
lift_step_setpoints = [i+.009 for i in lift_level_setpoints]
