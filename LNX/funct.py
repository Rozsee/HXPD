# -*- coding: utf-8 -*-
"""
#########################
LINUX VERSION use on RPi
#########################

Created on Fri Jan 26 21:27:17 2018
@author: Rozsee
"""
import pygame
import sys

import IK
import obj

from IK import HeadMovInput, HeadCalibrVal, HeadMovOutput

global CmdBuf
CmdBuf = ""                                                                     # globális válozo deklarása. Így kell, 2 sor...

"""DEFINITIONS, PROCEDURES..."""
def InitDS4():
    """ DualShock 4 init a pygmae joystick funkcióit alkalmazva"""
    print "FUNCT: Looking for joystick..."
    pygame.init()
    global ds4
    ds4 = pygame.joystick.Joystick(0)                                           # Controller init
    ds4.init() 
    print "FUNCT: Joystick found..."
    print "FUNCT: InitDS4_OK"
    

def StopPrg(kematox):
    """ Leállítja a programot. Gracefull bontja a lapcsolatot a 
    DS4-el és lezárja a szervo kontroller által használt soros portot,
    majd kilép a programból"""
    pygame.joystick.quit()
    print "FUNCT: Joystick released...."
    pygame.quit()
    print "FUNCT: Pygame closed..."
    kematox.SRVCTRL.Port.close()
    print "FUNCT: Serial port released..."
    print "FUNCT: Exiting..."
    sys.exit()

def LookForDevices(kematox):
    if ds4.get_init() == True:
        joy_name = ds4.get_name()
        print "FUNCT: Controller name: " + joy_name
        joyBtnNmb = ds4.get_numbuttons()
        print "FUNCT: Number of buttons: " + str(joyBtnNmb)
        joyHtNmb = ds4.get_numhats()
        print "FUNCT: Number of hats: " + str(joyHtNmb) + "\n"
    else:
        print "FUNCT: Joystick not found, exiting..."
        StopPrg(kematox)
    kematox.SRVCTRL.Port.write("VER\r\n")
    version = kematox.SRVCTRL.Port.readline()
    kematox.SRVCTRL.Port.write("Q\r\n")
    resp = kematox.SRVCTRL.Port.readline()
    if resp == '.':
        print "FUNCT: SSC32-Servo controller found. Firmware version: " + version
        print "FUNCT: Ready\n"
    else:
        print "FUNCT: Servo controller not found, exiting..."
        StopPrg(kematox)

""" MOVEMENT RELATED DEFINITIONS """

def SetIdlePos(kematox, mode):
    """Default value for idle stance is "D"=275, "z"=48"""
    if mode == "set":
        IK.IK_SixLeg()
        kematox.MoveSixLeg(1000, "support")

    elif mode =="return":
        """STEP 1 - TRIPOD A lift legs"""
        IK.IK_in["POS_Z"] = -20.0
        IK.IK_Tripod_A("support")                       # A "swing" az IK_in_for Swing- et használja....
        kematox.MoveTripodA("default", "swing", 500)
       
        """STEP 2 - TRIPOD A lower leg to idle D position (275)"""
        IK.IK_in["D"] = 275.0
        IK.IK_in["POS_Z"] = 0
        IK.IK_Tripod_A("support")                       
        kematox.MoveTripodA("default", "swing", 500)
        
        """STEP 3 - TRIPOD B lift legs"""
        IK.IK_in["D"] = 225.0
        IK.IK_in["POS_Z"] = -30.0
        IK.IK_Tripod_B("support")                       
        kematox.MoveTripodB("default", "swing", 500)
        
        """STEP 4 - TRIPOD B lower leg to idle D position (275)"""
        IK.IK_in["D"] = 275.0
        IK.IK_in["POS_Z"] = 0
        IK.IK_Tripod_B("support")
        kematox.MoveTripodB("default", "swing", 500)
       
        """STEP 5 - lower body to idle position (z=48) """
        IK.IK_in["z"] = 48.0
        IK.IK_SixLeg()
        kematox.MoveSixLeg(1500, "support")

def SetReadyPos(kematox, mode):
    """Default values for ready stance "D"=225, "z"=110"""
    if mode == "set":
        """STEP 1 - Robor lift"""
        IK.IK_in["z"] = 110.0
        IK.IK_SixLeg()
        kematox.MoveSixLeg(1000, "swing")
        """STEP 2 - TRIPOD A lift legs"""
        IK.IK_in["POS_Z"] = -50.0
        IK.IK_Tripod_A("support")                       # A "swing" az IK_in_for Swing- et használja....
        kematox.MoveTripodA("default", "swing", 500)
        """STEP 3 - TRIPOD A lower legs"""
        IK.IK_in["D"] = 225.0
        IK.IK_in["POS_Z"] = 0
        IK.IK_Tripod_A("support")                       
        kematox.MoveTripodA("default", "swing", 500)
        """STEP 4 - TRIPOD B lift legs"""
        IK.IK_in["D"] = 275.0
        IK.IK_in["POS_Z"] = -50.0
        IK.IK_Tripod_B("support")                       
        kematox.MoveTripodB("default", "swing", 500)
        """STEP 5 - TRIPOD B lower legs"""
        IK.IK_in["D"] = 225.0
        IK.IK_in["POS_Z"] = 0
        IK.IK_Tripod_B("support")                       
        kematox.MoveTripodB("default", "swing", 500)
        """STEP 6 - TRIPOD A lift legs again to release stress in servos"""
        IK.IK_in["POS_Z"] = -25.0
        IK.IK_Tripod_A("support")                       # A "swing" az IK_in_for Swing- et használja....
        kematox.MoveTripodA("default", "swing", 500)
        """STEP 7 - TRIPOD A lower legs"""
        IK.IK_in["POS_Z"] = 0
        IK.IK_Tripod_A("support")                       
        kematox.MoveTripodA("default", "swing", 500)
        """STEP 8 - TRIPOD B lift legs again to release stress in servos"""
        IK.IK_in["POS_Z"] = -25.0
        IK.IK_Tripod_B("support")                       
        kematox.MoveTripodB("default", "swing", 500)
        """STEP 9 - TRIPOD B release legs"""
        IK.IK_in["POS_Z"] = 0
        IK.IK_Tripod_B("support")                       
        kematox.MoveTripodB("default", "swing", 500)
    elif mode == "return":
        """STEP 1 - return to default "z" at no matter what "D" value"""
        IK.IK_in["POS_Z"] = 0
        IK.IK_SixLeg()
        kematox.MoveSixLeg(None, "swing")
        """STEP 2 - TRIPOD A lift legs"""
        IK.IK_in["POS_Z"] = -25.0
        IK.IK_Tripod_A("support")                       # A "swing" az IK_in_for Swing- et használja....
        kematox.MoveTripodA("default", "swing", 500)
        """STEP 3 - TRIPOD A lower legs. "D" is now equals id default value"""
        IK.IK_in["D"] = 225.0
        IK.IK_in["POS_Z"] = 0
        IK.IK_Tripod_A("support")                       
        kematox.MoveTripodA("default", "swing", 500)
        """STEP 4 - TRIPOD B lift legs"""
        IK.IK_in["POS_Z"] = -25.0
        IK.IK_Tripod_B("support")                       
        kematox.MoveTripodB("default", "swing", 500)
        """STEP 5 - TRIPOD B lower legs"""
        IK.IK_in["POS_Z"] = 0
        IK.IK_Tripod_B("support")                       
        kematox.MoveTripodB("default", "swing", 500)

def IncreaseStance():
    pass

def DecresaeStance():
    pass
    
def TripodWalk(kematox, walkval):                    
    """ Tripod walkpattern """
    def defineStepHeight():
        """ check POS_Z value to deifne step high. In idle pos no walking allowed,
        if POS_Z is below or equal with the half of max. POS_Z value than 25mm stepHigh is allowed
        if POS_Z is more than than the half of the alloewed value than 50mm stephigh is allowed """
        z_saved = 0.0                                       # Z pozició mentésére szolgáló változó. Az emelés után a láb ehhez a z-hez tartozó magasságba áljon vissza.
        
        if IK.IK_in["POS_Z"] == 0:                               
            stepHeight = 0.0                                       
            return stepHeight
        elif IK.IK_in["POS_Z"] <= 65:                       # Az analog érétkek kerekítettek (-1 és 1 között 0,1-es lépésekben) ->meghatározott  
            stepHeight = -10.0                              # értéket vehet fel Z. ->az if feltételeket ehhez kell igazítani. Az 51 azért nem
            return stepHeight                               # müködött, mert ilyen értéket nem vehet fel Z ->mindig a nagyobb lépés teljesült...
        elif IK.IK_in["POS_Z"] > 65:                        # z lehetséges érétkei a pos_Hitec_to_JX.xls-ben találhatóak.
            stepHeight = -20.0                        
            return stepHeight

    if walkval["tripod_step_1_complete"] == False:             
        # 1. TRIPOD A support body and translates
        IK.IK_Tripod_A("support")
        kematox.MoveTripodA("default", "support", 750)
            
        # 2. TRIPOD B swigns -> raise and center TRIPOD B
        z_saved = IK.IK_in["POS_Z"]
        y_saved = IK.IK_in["POS_Y"]
        IK.IK_in["POS_Z"] = defineStepHeight()
        IK.IK_in["POS_X"] = 0.0
        IK.IK_in["POS_Y"] = 0.0
        IK.IK_in["ROT_Z"] = 0.0
        IK.IK_Tripod_B("support")                           # !!! swing-nél a még a régi IK dict van használatban !!!
        kematox.MoveTripodB("default", "swing", 750)
            
        # 3. TRIPOD B swings -> lowering TRIPOD B
        IK.IK_in["POS_Z"] = z_saved
        IK.IK_Tripod_B("support")                             # !!! swing-nél a még a régi IK dict van használatban !!!
        kematox.MoveTripodB("default", "swing", 1000)          #750
        
        walkval["tripod_step_1_complete"] = True
            
    elif walkval["tripod_step_1_complete"] == True:
        # 1. TRIPOD B support body and translates
        IK.IK_Tripod_B("support")
        kematox.MoveTripodB("default", "support", 750)
            
        # 2. TRIPOD A swigns -> raise TRIPOD A
        z_saved = IK.IK_in["POS_Z"]
        y_saved = IK.IK_in["POS_Y"]
        IK.IK_in["POS_Z"] = defineStepHeight()
        IK.IK_in["POS_X"] = 0.0                                 # new
        IK.IK_in["POS_Y"] = 0.0
        IK.IK_in["ROT_Z"] = 0.0
        IK.IK_Tripod_A("support")                             # !!! swing-nél a még a régi IK dict van használatban !!!
        kematox.MoveTripodA("default", "swing", 750)
            
        # 3. TRIPOD A swings -> lowering TRIPOD A
        IK.IK_in["POS_Z"] = z_saved
        IK.IK_Tripod_A("support")                             # !!! swing-nél a még a régi IK dict van használatban !!!
        kematox.MoveTripodA("default", "swing", 1000)         #750
        
        walkval["tripod_step_1_complete"] = False
        

def calc_POS_Z(input_dict, jbuff):
    z_minVal = input_dict["z"]
    z_maxVal = 240
    shifted_joy_minVal = 0
    shifted_joy_maxVal = 2
    
    pos_z = ((((z_maxVal - z_minVal) / (shifted_joy_maxVal -shifted_joy_minVal)) * jbuff["axis_R2"]) + z_minVal) - z_minVal
    return pos_z
    
def CenterHead(kematox):
    IK.CalcHeadPos(HeadMovInput, HeadCalibrVal, HeadMovOutput)
    kematox.MoveHead(HeadMovOutput, 500)

"""     
def LookForDevices(robot_inst, controller_inst):
    if controller_inst.get_init() == True:
        joy_name = controller_inst.get_name()
        print "FUNCT: Controller name: " + joy_name
        joyBtnNmb = controller_inst.get_numbuttons()
        print "FUNCT: Number of buttons: " + str(joyBtnNmb)
        joyHtNmb = controller_inst.get_numhats()
        print "FUNCT: Number of hats: " + str(joyHtNmb) + "\n"
    else:
        print "FUNCT: Joystick not found, exiting..."
        StopPrg(robot_inst)
    robot_inst.SRVCTRL.Port.write("VER\r\n")
    version = robot_inst.SRVCTRL.Port.readline()
    robot_inst.SRVCTRL.Port.write("Q\r\n")
    resp = robot_inst.SRVCTRL.Port.readline()
    if resp == '.':
        print "FUNCT: SSC32-Servo controller found. Firmware version: " + version
        print "FUNCT: Ready\n"
    else:
        print "FUNCT: Servo controller not found, exiting..."
        StopPrg(robot_inst)
"""