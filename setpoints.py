#mast setpoints
kMastBack = .0 #This is so the lift won't go up when the mast is back
kMastBackLimit = .0
kMastForwardLimit = 1

#claw setpoints
kOpen = .042
kClose = .771 #2/12/15 23.12: .771
kCan = .5
kTote = .5
kStall = 2 #This is for the current sensor.

#lift setpoints
kUp = .0 #This is so the mast won't tilt when the lift is up
kTop = .0
kBottom = 1
lift_level_setpoints = [kBottom, .7, .6, .5, .4, kTop]
