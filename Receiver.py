#-------------Setup----------------

import Ed
Ed.EdisonVersion = Ed.V2

Ed.DistanceUnits = Ed.CM

Ed.Tempo = Ed.TEMPO_MEDIUM
#--------setup-----------
tune = Ed.TuneString(150)
tunecount = 0
Ed.RegisterEventHandler(Ed.EVENT_TUNE_FINISHED, "TuneFinished")
Ed.RegisterEventHandler(Ed.EVENT_LINE_TRACKER_SURFACE_CHANGE, "SurfaceChange")
Ed.RegisterEventHandler(Ed.EVENT_LINE_TRACKER_ON_BLACK, "OnBlack")
Ed.RegisterEventHandler(Ed.EVENT_LINE_TRACKER_ON_WHITE, "OnWhite")
Ed.RegisterEventHandler(Ed.EVENT_KEYPAD_ROUND, "KeypadRound")
Ed.RegisterEventHandler(Ed.EVENT_KEYPAD_TRIANGLE, "KeypadTriangle")
Ed.RegisterEventHandler(Ed.EVENT_DRIVE_STRAIN, "DriveStrain")
Ed.RegisterEventHandler(Ed.EVENT_OBSTACLE_AHEAD, "ObstacleAhead")
Ed.RegisterEventHandler(Ed.EVENT_OBSTACLE_RIGHT, "ObstacleRight")
Ed.RegisterEventHandler(Ed.EVENT_OBSTACLE_LEFT, "ObstacleLeft")
Ed.RegisterEventHandler(Ed.EVENT_OBSTACLE_ANY, "ObstacleAny")
Ed.RegisterEventHandler(Ed.EVENT_CLAP_DETECTED, "ClapDetected")
Ed.RegisterEventHandler(Ed.EVENT_TIMER_FINISHED, "TimerFinished")
# ----- functions
def TuneFinished():
    Ed.SendIRData(188)
def SurfaceChange():
    Ed.SendIRData(189)
def OnBlack():
    Ed.SendIRData(190)    
def OnWhite():
    Ed.SendIRData(191)
def KeypadRound():
    Ed.SendIRData(192)
def KeypadTriangle():
    Ed.SendIRData(193)
def DriveStrain():
    Ed.SendIRData(194)
def ObstacleAhead():
    Ed.SendIRData(195)
def ObstacleRight():
    Ed.SendIRData(196)
def ObstacleLeft():
    Ed.SendIRData(197)
def ObstacleAny():
    Ed.SendIRData(198)
def ClapDetected():
    Ed.SendIRData(199)
def TimerFinished():
    Ed.SendIRData(200)
def Complete():
    Ed.SendIRData(2)
def Error():
    Ed.SendIRData(8)
def Wait():
    Ed.TimeWait(100, Ed.TIME_MILLISECONDS)
# -- matching engine ----
Ed.ReadIRData()
while True:
        #get new data
        processing = Ed.ReadIRData()
        #begin special
        if processing == 3:
            Ed.PlayTune(tune)
            Complete()
        if processing == 4:
            tunecount = 0
            Complete()
        if processing == 9:
            Ed.Drive(Ed.STOP, Ed.STOP, 0)
            Complete()
            
        #begin movement
        if processing == 10:
            Wait()
            Ed.Drive(Ed.FORWARD, Ed.SPEED_1, Ed.ReadIRData())   
            Complete()
        if processing == 11:
            Wait()
            Ed.Drive(Ed.FORWARD, Ed.SPEED_2, Ed.ReadIRData())  
            Complete()
        if processing == 12:
            Wait()
            Ed.Drive(Ed.FORWARD, Ed.SPEED_3, Ed.ReadIRData())
            Complete()
        if processing == 13:
            Wait()
            Ed.Drive(Ed.FORWARD, Ed.SPEED_4, Ed.ReadIRData()) 
            Complete()
        if processing == 14:
            Wait()
            Ed.Drive(Ed.FORWARD, Ed.SPEED_5, Ed.ReadIRData())   
            Complete()
        if processing == 15:
            Wait()
            Ed.Drive(Ed.FORWARD, Ed.SPEED_6, Ed.ReadIRData())   
            Complete()
        if processing == 16:
            Wait()
            Ed.Drive(Ed.FORWARD, Ed.SPEED_7, Ed.ReadIRData()) 
            Complete()
        if processing == 17:
            Wait()
            Ed.Drive(Ed.FORWARD, Ed.SPEED_8, Ed.ReadIRData())   
            Complete()
        if processing == 18:
            Wait()
            Ed.Drive(Ed.FORWARD, Ed.SPEED_9, Ed.ReadIRData())   
            Complete()
        if processing == 19:
            Wait()
            Ed.Drive(Ed.FORWARD, Ed.SPEED_10, Ed.ReadIRData())        
            Complete()
        if processing == 20:
            Wait()
            Ed.Drive(Ed.BACKWARD, Ed.SPEED_1, Ed.ReadIRData())        
            Complete()
        if processing == 21:
            Wait()
            Ed.Drive(Ed.BACKWARD, Ed.SPEED_2, Ed.ReadIRData())        
            Complete()
        if processing == 22:
            Wait()
            Ed.Drive(Ed.BACKWARD, Ed.SPEED_3, Ed.ReadIRData())
            Complete()
        if processing == 23:           
            Wait()
            Ed.Drive(Ed.BACKWARD, Ed.SPEED_4, Ed.ReadIRData())
            Complete()
        if processing == 24:
            Wait()
            Ed.Drive(Ed.BACKWARD, Ed.SPEED_5, Ed.ReadIRData())        
            Complete()
        if processing == 25:
            Wait()
            Ed.Drive(Ed.BACKWARD, Ed.SPEED_6, Ed.ReadIRData())        
            Complete()
        if processing == 26:
            Wait()
            Ed.Drive(Ed.BACKWARD, Ed.SPEED_7, Ed.ReadIRData())        
            Complete()
        if processing == 27:
            Wait()
            Ed.Drive(Ed.BACKWARD, Ed.SPEED_8, Ed.ReadIRData())
            Complete()
        if processing == 28:
            Wait()
            Ed.Drive(Ed.BACKWARD, Ed.SPEED_9, Ed.ReadIRData())
            Complete()
        if processing == 29:
            Wait()
            Ed.Drive(Ed.BACKWARD, Ed.SPEED_10, Ed.ReadIRData())
            Complete()
        if processing == 30:
            Wait()
            Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_1, Ed.ReadIRData())
            Complete()
        if processing == 31:
            Wait()
            Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_2, Ed.ReadIRData())
            Complete()
        if processing == 32:
            Wait()
            Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_3, Ed.ReadIRData())
            Complete()
        if processing == 33:
            Wait()
            Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_4, Ed.ReadIRData())
            Complete()
        if processing == 34:
            Wait()
            Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_5, Ed.ReadIRData())
            Complete()
        if processing == 35:
            Wait()
            Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_6, Ed.ReadIRData())
            Complete()
        if processing == 36:
            Wait()
            Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_7, Ed.ReadIRData())
            Complete()
        if processing == 37:
            Wait()
            Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_8, Ed.ReadIRData())
            Complete()
        if processing == 38:
            Wait()
            Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_9, Ed.ReadIRData())
            Complete()
        if processing == 39:
            Wait()
            Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_10, Ed.ReadIRData())
            Complete()
        if processing == 40:
            Wait()
            Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_1, Ed.ReadIRData())
            Complete()
        if processing == 41:
            Wait()
            Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_2, Ed.ReadIRData())
            Complete()
        if processing == 42:
            Wait()
            Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_3, Ed.ReadIRData())
            Complete()
        if processing == 43:
            Wait()
            Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_4, Ed.ReadIRData())
            Complete()
        if processing == 44:
            Wait()
            Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_5, Ed.ReadIRData())
            Complete()
        if processing == 45:
            Wait()
            Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_6, Ed.ReadIRData())
            Complete()
        if processing == 46:
            Wait()
            Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_7, Ed.ReadIRData())
            Complete()
        if processing == 47:
            Wait()
            Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_8, Ed.ReadIRData())
            Complete()
        if processing == 48:
            Wait()
            Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_9, Ed.ReadIRData())
            Complete()
        if processing == 49:
            Wait()
            Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_10, Ed.ReadIRData())
            Complete()
        if processing == 50:
            Wait()
            Ed.Drive(Ed.FORWARD_LEFT, Ed.SPEED_1, Ed.ReadIRData())
            Complete()
        if processing == 51:
            Wait()
            Ed.Drive(Ed.FORWARD_LEFT, Ed.SPEED_2, Ed.ReadIRData())
            Complete()
        if processing == 52:
            Wait()
            Ed.Drive(Ed.FORWARD_LEFT, Ed.SPEED_3, Ed.ReadIRData())
            Complete()
        if processing == 53:
            Wait()
            Ed.Drive(Ed.FORWARD_LEFT, Ed.SPEED_4, Ed.ReadIRData())
            Complete()
        if processing == 54:
            Wait()
            Ed.Drive(Ed.FORWARD_LEFT, Ed.SPEED_5, Ed.ReadIRData())
            Complete()
        if processing == 55:
            Wait()
            Ed.Drive(Ed.FORWARD_LEFT, Ed.SPEED_6, Ed.ReadIRData())
            Complete()
        if processing == 56:
            Wait()
            Ed.Drive(Ed.FORWARD_LEFT, Ed.SPEED_7, Ed.ReadIRData())
            Complete()
        if processing == 57:
            Wait()
            Ed.Drive(Ed.FORWARD_LEFT, Ed.SPEED_8, Ed.ReadIRData())
            Complete()
        if processing == 58:
            Wait()
            Ed.Drive(Ed.FORWARD_LEFT, Ed.SPEED_9, Ed.ReadIRData())
            Complete()
        if processing == 59:
            Wait()
            Ed.Drive(Ed.FORWARD_LEFT, Ed.SPEED_10, Ed.ReadIRData())
            Complete()
        if processing == 60:
            Wait()
            Ed.Drive(Ed.FORWARD_RIGHT, Ed.SPEED_1, Ed.ReadIRData())
            Complete()
        if processing == 61:
            Wait()
            Ed.Drive(Ed.FORWARD_RIGHT, Ed.SPEED_2, Ed.ReadIRData())
            Complete()
        if processing == 62:
            Wait()
            Ed.Drive(Ed.FORWARD_RIGHT, Ed.SPEED_3, Ed.ReadIRData())
            Complete()
        if processing == 63:
            Wait()
            Ed.Drive(Ed.FORWARD_RIGHT, Ed.SPEED_4, Ed.ReadIRData())
            Complete()
        if processing == 64:
            Wait()
            Ed.Drive(Ed.FORWARD_RIGHT, Ed.SPEED_5, Ed.ReadIRData())
            Complete()
        if processing == 65:
            Wait()
            Ed.Drive(Ed.FORWARD_RIGHT, Ed.SPEED_6, Ed.ReadIRData())
            Complete()
        if processing == 66:
            Wait()
            Ed.Drive(Ed.FORWARD_RIGHT, Ed.SPEED_7, Ed.ReadIRData())
            Complete()
        if processing == 67:
            Wait()
            Ed.Drive(Ed.FORWARD_RIGHT, Ed.SPEED_8, Ed.ReadIRData())
            Complete()
        if processing == 68:
            Wait()
            Ed.Drive(Ed.FORWARD_RIGHT, Ed.SPEED_9, Ed.ReadIRData())
            Complete()
        if processing == 69:
            Wait()
            Ed.Drive(Ed.FORWARD_RIGHT, Ed.SPEED_10, Ed.ReadIRData())
            Complete()
        if processing == 70:
            Wait()
            Ed.Drive(Ed.BACKWARD_LEFT, Ed.SPEED_1, Ed.ReadIRData())
            Complete()
        if processing == 71:
            Wait()
            Ed.Drive(Ed.BACKWARD_LEFT, Ed.SPEED_2, Ed.ReadIRData())
            Complete()
        if processing == 72:
            Wait()
            Ed.Drive(Ed.BACKWARD_LEFT, Ed.SPEED_3, Ed.ReadIRData())
            Complete()
        if processing == 73:
            Wait()
            Ed.Drive(Ed.BACKWARD_LEFT, Ed.SPEED_4, Ed.ReadIRData())
            Complete()
        if processing == 74:
            Wait()
            Ed.Drive(Ed.BACKWARD_LEFT, Ed.SPEED_5, Ed.ReadIRData())
            Complete()
        if processing == 75:
            Wait()
            Ed.Drive(Ed.BACKWARD_LEFT, Ed.SPEED_6, Ed.ReadIRData())
            Complete()
        if processing == 76:
            Wait()
            Ed.Drive(Ed.BACKWARD_LEFT, Ed.SPEED_7, Ed.ReadIRData())
            Complete()
        if processing == 77:
            Wait()
            Ed.Drive(Ed.BACKWARD_LEFT, Ed.SPEED_8, Ed.ReadIRData())
            Complete()
        if processing == 78:
            Wait()
            Ed.Drive(Ed.BACKWARD_LEFT, Ed.SPEED_9, Ed.ReadIRData())
            Complete()
        if processing == 79:
            Wait()
            Ed.Drive(Ed.BACKWARD_LEFT, Ed.SPEED_10, Ed.ReadIRData())
            Complete()
        if processing == 80:
            Wait()
            Ed.Drive(Ed.BACKWARD_RIGHT, Ed.SPEED_1, Ed.ReadIRData())
            Complete()
        if processing == 81:
            Wait()
            Ed.Drive(Ed.BACKWARD_RIGHT, Ed.SPEED_2, Ed.ReadIRData())
            Complete()
        if processing == 82:
            Wait()
            Ed.Drive(Ed.BACKWARD_RIGHT, Ed.SPEED_3, Ed.ReadIRData())
            Complete()
        if processing == 83:
            Wait()
            Ed.Drive(Ed.BACKWARD_RIGHT, Ed.SPEED_4, Ed.ReadIRData())
            Complete()
        if processing == 84:
            Wait()
            Ed.Drive(Ed.BACKWARD_RIGHT, Ed.SPEED_5, Ed.ReadIRData())
            Complete()
        if processing == 85:
            Wait()
            Ed.Drive(Ed.BACKWARD_RIGHT, Ed.SPEED_6, Ed.ReadIRData())
            Complete()
        if processing == 86:
            Wait()
            Ed.Drive(Ed.BACKWARD_RIGHT, Ed.SPEED_7, Ed.ReadIRData())
            Complete()
        if processing == 87:
            Wait()
            Ed.Drive(Ed.BACKWARD_RIGHT, Ed.SPEED_8, Ed.ReadIRData())
            Complete()
        if processing == 88:
            Wait()
            Ed.Drive(Ed.BACKWARD_RIGHT, Ed.SPEED_9, Ed.ReadIRData())
            Complete()
        if processing == 89:
            Wait()
            Ed.Drive(Ed.BACKWARD_RIGHT, Ed.SPEED_10, Ed.ReadIRData())
            Complete()
        #begin music
        if processing == 233:
            tune[tunecount] = "m"
            tunecount = tunecount + 1
            Complete()
        if processing == 234:
            tune[tunecount] = "M"
            tunecount = tunecount + 1    
            Complete()
        if processing == 235:
            tune[tunecount] = "n"
            tunecount = tunecount + 1
            Complete()
        if processing == 236:
            tune[tunecount] = "c"
            tunecount = tunecount + 1
            Complete()
        if processing == 237:
            tune[tunecount] = "C"
            tunecount = tunecount + 1
            Complete()
        if processing == 238:
            tune[tunecount] = "d"
            tunecount = tunecount + 1  
            Complete()
        if processing == 239:
            tune[tunecount] = "D"
            tunecount = tunecount + 1
            Complete()
        if processing == 240:
            tune[tunecount] = "e"
            tunecount = tunecount + 1
            Complete()
        if processing == 241:
            tune[tunecount] = "f"
            tunecount = tunecount + 1
            Complete()
        if processing == 242:
            tune[tunecount] = "F"
            tunecount = tunecount + 1    
            Complete()
        if processing == 243:
            tune[tunecount] = "g"
            tunecount = tunecount + 1
            Complete()
        if processing == 244:
            tune[tunecount] = "G"
            tunecount = tunecount + 1
            Complete()
        if processing == 245:
            tune[tunecount] = "a"
            tunecount = tunecount + 1
            Complete()
        if processing == 246:
            tune[tunecount] = "A"
            tunecount = tunecount + 1  
            Complete()
        if processing == 247:
            tune[tunecount] = "b"
            tunecount = tunecount + 1
            Complete()
        if processing == 248:
            tune[tunecount] = "o"
            tunecount = tunecount + 1
            Complete()
        if processing == 249:
            tune[tunecount] = "1"
            tunecount = tunecount + 1
            Complete()
        if processing == 250:
            tune[tunecount] = "2"
            tunecount = tunecount + 1    
            Complete()
        if processing == 251:
            tune[tunecount] = "4"
            tunecount = tunecount + 1
            Complete()
        if processing == 252:
            tune[tunecount] = "8"
            tunecount = tunecount + 1
            Complete()
        if processing == 253:
            tune[tunecount] = "6"
            tunecount = tunecount + 1
            Complete()
        if processing == 254:
            tune[tunecount] = "R"
            tunecount = tunecount + 1  
            Complete()
        if processing == 255:
            tune[tunecount] = "z"
            tunecount = tunecount + 1
            Complete()
