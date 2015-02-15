#Note to self - don't EVER disassemble the mast. Doesn't end well.
#mast setpoints - 2/13/15
kMastBack = .301 #This is so the lift won't go up when the mast is back - DO NOT CHANGE IN TESTING
kMastBackLimit = .285
kMastForwardLimit = .445
kMastParallel = .416

#claw setpoints - tested 2/12/15
kOpen = .237
kClose = .976 #2/12/15 23.12: .771 2/13/15 16:30: .925 2/15/15 .070
kCan = .375
kTote = .545
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
