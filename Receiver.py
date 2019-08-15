
#-------------Setup----------------

import Ed
Ed.EdisonVersion = Ed.V2

Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM

#--------setup-----------
tune = Ed.TuneString(150)
tunecount = 0

# ----- test send a start

#nothing here right now

# -- matching engine ----
Ed.ReadIRData()
while True:
        processing = Ed.ReadIRData()
        #begin special
        if processing == 3:
            Ed.PlayTune(tune)
        if processing == 4:
            tunecount = 0

        #begin movement
        if processing == 10:
            Ed.Drive(Ed.FORWARD, Ed.SPEED_1, Ed.ReadIRData())   
        if processing == 11:
            Ed.Drive(Ed.FORWARD, Ed.SPEED_2, Ed.ReadIRData())   
        if processing == 12:
            Ed.Drive(Ed.FORWARD, Ed.SPEED_3, Ed.ReadIRData())   
        if processing == 13:
            Ed.Drive(Ed.FORWARD, Ed.SPEED_4, Ed.ReadIRData()) 
        if processing == 14:
            Ed.Drive(Ed.FORWARD, Ed.SPEED_5, Ed.ReadIRData())   
        if processing == 15:
            Ed.Drive(Ed.FORWARD, Ed.SPEED_6, Ed.ReadIRData())   
        if processing == 16:
            Ed.Drive(Ed.FORWARD, Ed.SPEED_7, Ed.ReadIRData()) 
        if processing == 17:
            Ed.Drive(Ed.FORWARD, Ed.SPEED_8, Ed.ReadIRData())   
        if processing == 18:
            Ed.Drive(Ed.FORWARD, Ed.SPEED_9, Ed.ReadIRData())   
        if processing == 19:
            Ed.Drive(Ed.FORWARD, Ed.SPEED_10, Ed.ReadIRData())        
        if processing == 20:
            Ed.Drive(Ed.BACKWARD, Ed.SPEED_1, Ed.ReadIRData())        
        if processing == 21:
            Ed.Drive(Ed.BACKWARD, Ed.SPEED_2, Ed.ReadIRData())        
        if processing == 22:
            Ed.Drive(Ed.BACKWARD, Ed.SPEED_3, Ed.ReadIRData())
        if processing == 23:           
            Ed.Drive(Ed.BACKWARD, Ed.SPEED_4, Ed.ReadIRData())
        if processing == 24:
            Ed.Drive(Ed.BACKWARD, Ed.SPEED_5, Ed.ReadIRData())        
        if processing == 25:
            Ed.Drive(Ed.BACKWARD, Ed.SPEED_6, Ed.ReadIRData())        
        if processing == 26:
            Ed.Drive(Ed.BACKWARD, Ed.SPEED_7, Ed.ReadIRData())        
        if processing == 27:
            Ed.Drive(Ed.BACKWARD, Ed.SPEED_8, Ed.ReadIRData())
        if processing == 28:
            Ed.Drive(Ed.BACKWARD, Ed.SPEED_9, Ed.ReadIRData())
        if processing == 29:
            Ed.Drive(Ed.BACKWARD, Ed.SPEED_10, Ed.ReadIRData())
        if processing == 30:
            Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_1, Ed.ReadIRData())
        if processing == 31:
            Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_2, Ed.ReadIRData())
        if processing == 32:
            Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_3, Ed.ReadIRData())
        if processing == 33:
            Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_4, Ed.ReadIRData())
        if processing == 34:
            Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_5, Ed.ReadIRData())
        if processing == 35:
            Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_6, Ed.ReadIRData())
        if processing == 36:
            Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_7, Ed.ReadIRData())
        if processing == 37:
            Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_8, Ed.ReadIRData())
        if processing == 38:
            Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_9, Ed.ReadIRData())
        if processing == 39:
            Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_10, Ed.ReadIRData())
        if processing == 40:
            Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_1, Ed.ReadIRData())
        if processing == 41:
            Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_2, Ed.ReadIRData())
        if processing == 42:
            Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_3, Ed.ReadIRData())
        if processing == 43:
            Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_4, Ed.ReadIRData())
        if processing == 44:
            Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_5, Ed.ReadIRData())
        if processing == 45:
            Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_6, Ed.ReadIRData())
        if processing == 46:
            Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_7, Ed.ReadIRData())
        if processing == 47:
            Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_8, Ed.ReadIRData())
        if processing == 48:
            Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_9, Ed.ReadIRData())
        if processing == 49:
            Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_10, Ed.ReadIRData())
        
        #begin music
        if processing == 233:
            tune[tunecount] = "m"
            tunecount = tunecount + 1
        if processing == 234:
            tune[tunecount] = "M"
            tunecount = tunecount + 1    
        if processing == 235:
            tune[tunecount] = "n"
            tunecount = tunecount + 1
        if processing == 236:
            tune[tunecount] = "c"
            tunecount = tunecount + 1
        if processing == 237:
            tune[tunecount] = "C"
            tunecount = tunecount + 1
        if processing == 238:
            tune[tunecount] = "d"
            tunecount = tunecount + 1  
        if processing == 239:
            tune[tunecount] = "D"
            tunecount = tunecount + 1
        if processing == 240:
            tune[tunecount] = "e"
            tunecount = tunecount + 1
        if processing == 241:
            tune[tunecount] = "f"
            tunecount = tunecount + 1
        if processing == 242:
            tune[tunecount] = "F"
            tunecount = tunecount + 1    
        if processing == 243:
            tune[tunecount] = "g"
            tunecount = tunecount + 1
        if processing == 244:
            tune[tunecount] = "G"
            tunecount = tunecount + 1
        if processing == 245:
            tune[tunecount] = "a"
            tunecount = tunecount + 1
        if processing == 246:
            tune[tunecount] = "A"
            tunecount = tunecount + 1  
        if processing == 247:
            tune[tunecount] = "b"
            tunecount = tunecount + 1
        if processing == 248:
            tune[tunecount] = "o"
            tunecount = tunecount + 1
        if processing == 249:
            tune[tunecount] = "1"
            tunecount = tunecount + 1
        if processing == 250:
            tune[tunecount] = "2"
            tunecount = tunecount + 1    
        if processing == 251:
            tune[tunecount] = "4"
            tunecount = tunecount + 1
        if processing == 252:
            tune[tunecount] = "8"
            tunecount = tunecount + 1
        if processing == 253:
            tune[tunecount] = "6"
            tunecount = tunecount + 1
        if processing == 254:
            tune[tunecount] = "R"
            tunecount = tunecount + 1  
        if processing == 255:
            tune[tunecount] = "z"
            tunecount = tunecount + 1
        
        
        
        
        
        
