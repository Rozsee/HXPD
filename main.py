# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 15:47:59 2017

@author: Rozsee
""" 
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import obj
import funct
import IK
import time
from copy import deepcopy
from IK import IK_in, IK_in_for_Swing, IK_Tripod_A, IK_Tripod_B


""" VARIABLE DECLARATIONS """
modeVal = {"mode": 0, "prev_mode": 0 }
joyVal = {"PSBTN_counter": 0}
flags = {"position_reached": False, 
         "return_to_Ready": False, "return_to_Idle": False,
         "flag_thumbJoyStateChng_lx": False, "flag_thumbJoyStateChng_ly": False, 
         "flag_thumbJoyStateChng_rx": False, "flag_thumbJoyStateChng_ry": False,
         "flag_JoyStateChng_R2": False, "flag_shiftActivated": False,}
JoyBuffer = {"left_x": 0.0, "left_y": 0.0, "right_x": 0.0, "right_y": 0.0, "axis_R2": 0.0}
AxisBuffer ={
                "axis_lx": 0.0, "axis_ly": 0.0, "axis_rx": 0.0, "axis_ry": 0.0, "axis_L2": 0.0, "axis_R2":0.0,
                "prev_axis_lx": 0.0 , "prev_axis_ly": 0.0, "prev_axis_rx": 0.0, "prev_axis_ry": 0.0, "prev_axis_R2": 0.0,
                "lx_center": False, "ly_center": False, "rx_center": False, "ry_center": False, "R2_center": False
                
            }
auxVal = {"dist_to_grnd": 160.0, "lift_value": 35.0, "recoveryReq": False}

walkVal = {"tripod_substep": 0, "walkmode": "TRIPOD", "tripod_step_1_complete": False, "tripod_step_2_complete": False}

EVENT = None


    
def JoyButtonHandler(event):
    #print "DIAG: EVENT = JoyButtonHandler"
    for i in range(funct.ds4.get_numbuttons()):
        btn_ID = funct.ds4.get_button(i)                            
        if btn_ID == 1:                                                         # a button was pushed
            if i == 0: 
                event = "SQUARE"
            elif i == 1: 
                event = "CROSS"
            elif i == 2: 
                event = "CIRCLE"
            elif i == 3: 
                event = "TRIANGLE"
                EventDispatch(event, modeVal, IK_in, AxisBuffer, flags, auxVal)
            elif i == 4: 
                event = "L1"
            elif i == 5: 
                event = "R1"
                EventDispatch(event, modeVal, IK_in, AxisBuffer, flags, auxVal)
            elif i == 6: 
                event = "L2"
            elif i == 7: 
                event = "R2"
                EventDispatch(event, modeVal, IK_in, AxisBuffer, flags, auxVal)
            elif i == 8: 
                event = "SHARE"
            elif i == 9: 
                event = "OPTIONS"
                EventDispatch(event, modeVal, IK_in, AxisBuffer, flags, auxVal)
            elif i == 10: 
                event = "LEFT THUMB. BTN."
            elif i == 11: 
                event = "RIGHT THUMB. BTN."
            elif i == 12: 
                event = "PSBTN"
                EventDispatch(event, modeVal, IK_in, AxisBuffer, flags, auxVal)
            elif i == 13: 
                event = "TOUCH SCREEN"
    
    
def ThumbJoyHandler(jbuff, axisbuff, flag_dict, event):
    axisbuff["axis_lx"] = funct.ds4.get_axis(0) * -1                                # Bal oldali thumbjoy az x és y tengel menti forgásokat adja
    if abs(axisbuff["axis_lx"]) < 0.1:
        if axisbuff["lx_center"] == False:
            axisbuff["axis_lx"] = 0
            jbuff["left_x"] = axisbuff["axis_lx"]
            axisbuff["lx_center"] = True
            flag_dict["flag_thumbJoyStateChng_lx"] = True
        elif axisbuff["lx_center"] == True:
            flag_dict["flag_thumbJoyStateChng_lx"] = False
    elif abs(axisbuff["axis_lx"]) > 0.1:
        if axisbuff["axis_lx"] != axisbuff["prev_axis_lx"]:
            axisbuff["prev_axis_lx"] = axisbuff["axis_lx"]
            jbuff["left_x"] = axisbuff["axis_lx"]
            axisbuff["lx_center"] = False
            flag_dict["flag_thumbJoyStateChng_lx"] = True
        else:
            flag_dict["flag_thumbJoyStateChng_lx"] = False
    
    axisbuff["axis_ly"] = funct.ds4.get_axis(1)
    if abs(axisbuff["axis_ly"]) < 0.1:
        if axisbuff["ly_center"] == False:
            axisbuff["axis_ly"] = 0
            jbuff["left_y"] = axisbuff["axis_ly"]
            axisbuff["ly_center"] = True
            flag_dict["flag_thumbJoyStateChng_ly"] = True
        elif axisbuff["ly_center"] == True:
            flag_dict["flag_thumbJoyStateChng_ly"] = False
    elif abs(axisbuff["axis_ly"]) > 0.1:
        if axisbuff["axis_ly"] != axisbuff["prev_axis_ly"]:
            axisbuff["prev_axis_ly"] = axisbuff["axis_ly"]
            jbuff["left_y"] = axisbuff["axis_ly"]
            axisbuff["ly_center"] = False
            flag_dict["flag_thumbJoyStateChng_ly"] = True
        else:
            flag_dict["flag_thumbJoyStateChng_ly"] = False

    axisbuff["axis_rx"] = funct.ds4.get_axis(2) * -1    
    if abs(axisbuff["axis_rx"]) < 0.1:
        if axisbuff["rx_center"] == False:
            axisbuff["axis_rx"] = 0
            jbuff["right_x"] = axisbuff["axis_rx"]
            axisbuff["rx_center"] = True
            flag_dict["flag_thumbJoyStateChng_rx"] = True
        elif axisbuff["rx_center"] == True:
            flag_dict["flag_thumbJoyStateChng_rx"] = False
    elif abs(axisbuff["axis_rx"]) > 0.1:
        if axisbuff["axis_rx"] != axisbuff["prev_axis_rx"]:
            axisbuff["prev_axis_rx"] = axisbuff["axis_rx"]
            jbuff["right_x"] = axisbuff["axis_rx"]
            axisbuff["rx_center"] = False
            flag_dict["flag_thumbJoyStateChng_rx"] = True
        else:
            flag_dict["flag_thumbJoyStateChng_rx"] = False

    axisbuff["axis_ry"] = funct.ds4.get_axis(3)
    if abs(axisbuff["axis_ry"]) < 0.1:
        if axisbuff["ry_center"] == False:
            axisbuff["axis_ry"] = 0
            jbuff["right_y"] = axisbuff["axis_ry"]
            axisbuff["ry_center"] = True
            flag_dict["flag_thumbJoyStateChng_ry"] = True
        elif axisbuff["ry_center"] == True:
            flag_dict["flag_thumbJoyStateChng_ry"] = False
    elif abs(axisbuff["axis_ry"]) > 0.1:
        if axisbuff["axis_ry"] != axisbuff["prev_axis_ry"]:
            axisbuff["prev_axis_ry"] = axisbuff["axis_ry"]
            jbuff["right_y"] = axisbuff["axis_ry"]
            axisbuff["ry_center"] = False
            flag_dict["flag_thumbJoyStateChng_ry"] = True
        else:
            flag_dict["flag_thumbJoyStateChng_ry"] = False
    
    
    axisbuff["axis_R2"] = funct.ds4.get_axis(4) + 1
    print str(axisbuff["axis_R2"])
    if axisbuff["axis_R2"] < 0.1:
        if axisbuff["R2_center"] == False:
            axisbuff["axis_R2"] = 0
            jbuff["axis_R2"] = axisbuff["axis_R2"]
            print "wiiiiiii"
            axisbuff["R2_center"] = True
            flag_dict["flag_JoyStateChng_R2"] = True
        elif axisbuff["R2_center"] == True:
            flag_dict["flag_JoyStateChng_R2"] = False
    elif axisbuff["axis_R2"] > 0.1:
        if axisbuff["axis_R2"] != axisbuff["prev_axis_R2"]:
            axisbuff["prev_axis_R2"] = axisbuff["axis_R2"]
            jbuff["axis_R2"] = axisbuff["axis_R2"]
            axisbuff["R2_center"] = False
            flag_dict["flag_JoyStateChng_R2"] = True
        else:
            flag_dict["flag_JoyStateChng_R2"] = False
    

    if flag_dict["flag_thumbJoyStateChng_lx"] or flag_dict["flag_thumbJoyStateChng_ly"] or flag_dict["flag_thumbJoyStateChng_rx"] or flag_dict["flag_thumbJoyStateChng_ry"] or flag_dict["flag_JoyStateChng_R2"] == True:
        event = "THMB_JOY"
        #print "THMB_JOYEVENT ---> THMB_JOYEVENT"
        EventDispatch(event, modeVal, IK_in, JoyBuffer, flags, auxVal)
        flag_dict["flag_thumbJoyStateChng"] = False
    
    
    
def EventSource():
    for event in funct.pygame.event.get():
        if event.type == funct.pygame.JOYBUTTONDOWN:
            JoyButtonHandler(EVENT)
            
        elif event.type == funct.pygame.JOYHATMOTION:           
            pass
            
        elif event.type == funct.pygame.JOYAXISMOTION:
            time.sleep(0.1) # szuresi kiserlet joymozgas was 0.15
            ThumbJoyHandler(JoyBuffer, AxisBuffer, flags, EVENT)
    
    
def EventDispatch(event, mode_dict, direction_dict, jbuff, flag_dict, auxval):
    if (event == "OPTIONS"):                                                    # HA az OPTIONS gombot megnyomtak,
        print "MAIN: Changing mode..."
        mode_dict["prev_mode"] = mode_dict["mode"]
        if mode_dict["prev_mode"] == 3:
            flag_dict["return_to_Ready"] = True
            
        mode_dict["mode"] = mode_dict["mode"] + 1                               # akkor a mode valtozot noveljuk
        if mode_dict["mode"] == 4:                                              # HA mode = 4 (ilyen mode nincs), akkor
            print "MAIN: Returning to READY..."
            mode_dict["mode"] = 1                                               # menjunk vissza READY mode-ba
            
        event = ""                                                              # EVENT valtozo torlese
        print "MAIN: Mode is: " + str(mode_dict["mode"])
        flag_dict["position_reached"] = False
        
    elif (event == "PSBTN"):                                                    # HA a PS gombot 1x megnyomjuk, akkor visszatérünk ready-be,                
        if mode_dict["mode"] == 1:
            print "MAIN: Returning to IDLE..."
            mode_dict["mode"] = 0
            event = ""
            flag_dict["return_to_Ready"] = False
            flag_dict["return_to_Idle"] = True
            flag_dict["position_reached"] = False
            
        else:
            print "MAIN: Returning to READY..."
            mode_dict["mode"] = 1
            event = ""
            flag_dict["return_to_Ready"] = True
            flag_dict["return_to_Idle"] = False
            flag_dict["position_reached"] = False
         
        """if mode_dict["mode"] == 1:
            print "MAIN: Returning to IDLE..."
            mode_dict["mode"] = 0
            event = ""
            flag_dict["position_reached"] = False
        else:
            print "MAIN: Returning to READY..."
            mode_dict["mode"] = 1
            flag_dict["return_to_Ready"] = True
            event = ""                                                          # végül a EVENT változót töröljük
            flag_dict["position_reached"] = False"""   
            
            
    elif (event == "THMB_JOY"):
        if mode_dict["mode"] == 2:                                              # Thmb joy analog ertekeinek allokálása "STATIC" mod esetén (2)
            if flag_dict["flag_shiftActivated"] == False:                       # HA SHIFT (Triangle button) nem aktív, akkor x, y tengely melntén forog, vagy "eltolodik" a robot
                direction_dict["ROT_X"] = 10 * jbuff["left_y"] 
                direction_dict["ROT_Z"] = 20 * jbuff["left_x"]                  #was 10
                direction_dict["POS_X"] = 50 * jbuff["right_x"] 
                direction_dict["POS_Y"] = 50 * jbuff["right_y"]
                direction_dict["POS_Z"] = funct.calc_POS_Z(IK_in, jbuff)
                flag_dict["position_reached"] = False
            elif flag_dict["flag_shiftActivated"] == True:                      # HA SHIFT (Triangle button) aktív, akkor x,y mentén "eltolódik a robot, illetve Z tengely mentén fordúl
                direction_dict["POS_X"] = 50 * jbuff["right_x"] 
                direction_dict["POS_Y"] = 50 * jbuff["right_y"]
                direction_dict["ROT_Y"] = 10 * jbuff["left_x"]
                direction_dict["POS_Z"] = funct.calc_POS_Z(IK_in, jbuff)
                flag_dict["position_reached"] = False
                    
        elif mode_dict["mode"] == 3:
            direction_dict["POS_X"] = 50 * jbuff["right_x"] 
            direction_dict["POS_Y"] = 50 * jbuff["right_y"]
            direction_dict["POS_Z"] = funct.calc_POS_Z(IK_in, jbuff)
     
    
    
    elif (event == "TRIANGLE"):
        if mode_dict["mode"] == 2 or 3:
            if flag_dict["flag_shiftActivated"] == False:
                flag_dict["flag_shiftActivated"] = True
                print "SHIFT is ON"
            elif flag_dict["flag_shiftActivated"] == True:
                flag_dict["flag_shiftActivated"] = False
                print "SHIFT is OFF"
            

def EventExecute(event, mode_dict, flag_dict, auxval, walkval):
    if mode_dict["mode"] == 0: # IDLE
        if flag_dict["position_reached"] == False:
            if flag_dict["return_to_Idle"] == True:
                print "MAIN: Returning to IDLE"
                kematox.return_to_Idle()
                print "MAIN: IDLE position reached\n"
                flag_dict["return_to_Idle"] = False
                flag_dict["position_reached"] = True
            
            elif flag_dict["return_to_Idle"] == False:
                print "MAIN: MODE set to IDLE"                                  # ide még a fejet idle-be parancsot be kell szúrni
                #kematox.SetUpIdle()                                             # Kezdo, leultetett allapot felvetele
                
                funct.SetIdlePos(kematox)
                              
                print "MAIN: IDLE position reached\n"
                flag_dict["position_reached"] = True
                
        elif flag_dict["position_reached"] == True:
            pass
            
    elif mode_dict["mode"] == 1: # READY
        if flag_dict["position_reached"] == False:
            if flag_dict["return_to_Ready"] == True:
                print "MAIN: Returning to READY"
                
                funct.SetReadyPos(kematox, "return")
                
                #kematox.return_to_Ready()
                #IK_in["POS_Z"] = 0.0
                #auxval["dist_to_grnd"] = 160.0                                  # A magasság jelzo valtozo visszairasa a default értékre                
                print "MAIN: READY position reached\n"
                flag_dict["return_to_Ready"] = False
                flag_dict["position_reached"] = True
                
            elif flag_dict["return_to_Ready"] == False:
                print "MAIN: MODE set to READY"
                
                funct.SetReadyPos(kematox, "set")
                
                #kematox.go_to_Ready()
                #kematox.go_to_Ready_v2()
                print "MAIN: READY position reached\n"
                flag_dict["position_reached"] = True
                
        elif flag_dict["position_reached"] == True:
            pass
            
    elif mode_dict["mode"] == 2: # STATIC
        if flag_dict["position_reached"] == False:
            IK.IK_SixLeg()
            kematox.use_IK_calc("support")
            #IK.IK_Diag(IK.IK_out)
            flag_dict["position_reached"] = True
            print "DIAG: MOVEMENT READY"
        elif flag_dict["position_reached"] == True:
            pass
        
    elif mode_dict["mode"] == 3: # WALK
        #kematox.return_to_Ready()
        if walkval["walkmode"] == "TRIPOD":
            WalkVector = IK.CalcWalkVector()
            #print "WalkVector = " + str(WalkVector)
            if WalkVector > 0: 
                # -----STEP_1------
                IK_Tripod_A("support")
                kematox.MoveTripodA("default", "support", 750)
                IK.IK_Calc_SwingLegs(IK_in_for_Swing, auxVal, "up")         # creates IK_in_for_Swing with modified coordinates
                IK_Tripod_B("swing")                                        # creates TripodB_MoveTable according to IK_in_for_Swing 
                kematox.MoveTripodB("default", "swing", 750)                # executes movement according to TripodB_MoveTable
                IK.IK_Calc_SwingLegs(IK_in_for_Swing, auxVal, "down")
                IK_Tripod_B("swing") 
                kematox.MoveTripodB("default", "swing", 750) 
                # -----STEP_2------
                IK_Tripod_B("support")
                kematox.MoveTripodB("default", "support", 750)
                IK.IK_Calc_SwingLegs(IK_in_for_Swing, auxVal, "up")
                IK_Tripod_A("swing") 
                kematox.MoveTripodA("default", "swing", 750) 
                IK.IK_Calc_SwingLegs(IK_in_for_Swing, auxVal, "down")
                IK_Tripod_A("swing")
                kematox.MoveTripodA("default", "swing", 750)
            else:
                pass
     
    
""" PROGRAM START """   
kematox = obj.Hexapod("kematox")
funct.InitDS4()
funct.LookForDevices(kematox) 

while (True):
    try:
        EventSource()
        EventExecute(EVENT, modeVal, flags, auxVal, walkVal)
        
    except KeyboardInterrupt:
        funct.StopPrg(kematox)