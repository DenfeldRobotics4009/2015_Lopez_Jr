#mast setpoints - 2/13/15
kMastBack = .275 #This is so the lift won't go up when the mast is back
kMastBackLimit = .275
kMastForwardLimit = .437
kMastParallel = .416

#claw setpoints - tested 2/12/15
kOpen = .227
kClose = .925 #2/12/15 23.12: .771 2/13/15 16:30: .925
kCan = .375
kTote = .505
kStall = 2 #This is for the current sensor.

#lift setpoints - untested
#Tote=.104
#kUp = .637 #This is so the mast won't tilt when the lift is up
#kTop = .863 #was .651
#kBottom = .050
#kDelta = (kTop-kBottom)
#lift_level_setpoints = [kBottom, (kDelta*(.115+kBottom)), (kDelta*(.275+kBottom)),
#        (kDelta*(.435+kBottom)), (kDelta*(.594+kBottom)), (kDelta*(.753+kBottom)),
 #       (kDelta*(.913+kBottom)), kTop]
#lift_step_setpoints = [i+.009 for i in lift_level_setpoints]
lift_level_setpoints = [.11, .12]
