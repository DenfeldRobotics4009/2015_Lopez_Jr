__author__ = 'nikolojedison'
#Temporary copypasta from robot.py, since I'm doing some housekeeping
#over there. -Nik    
    
    auto = Auto(self)
        three_tote = self.smart_dashboard.getBoolean("3 Tote Auto", defaultValue=False) #If the dashboard hasn't set the value, it's False by default.
        test_switch = self.smart_dashboard.getBoolean("Test Switch", defaultValue=False)

        self.drive.setSafetyEnabled(False)

        if three_tote:
            #Do the thing if the button's pushed
            auto.tote_grabba()
            auto.tote_lift(1)
            auto.can_slappa()
            auto.forward(1)
            auto.tote_releasa()
            auto.tote_lower(1)
            auto.tote_grabba()
            auto.tote_lift(1)
            auto.can_slappa()
            auto.forward(1)
            auto.tote_releasa()
            auto.tote_lower(1)
            auto.tote_grabba()
            auto.tote_lift(1)

        elif auto_program_two: #this is the simple auton that was talked about.
            auto.forward(5)
        else:
            pass
            #Neither are pushed