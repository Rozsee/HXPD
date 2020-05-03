# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 21:27:17 2018

@author: Rozsee
"""
import pygame
import sys

import IK
import obj


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

def SetIdlePos(kematox):
    """Default value for idle stance is "D"=275, "z"=48"""
    IK.IK_SixLeg()
    kematox.use_IK_calc("support")

def SetReadyPos(kematox, mode):
    """Default values for ready stance "D"=225, "z"=110"""
    if mode == "set":
        """STEP 1 - Robor lift"""
        IK.IK_in["z"] = 110.0
        IK.IK_SixLeg()
        kematox.use_IK_calc("swing")
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
        kematox.use_IK_calc("swing")
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
    

def calc_POS_Z(input_dict, jbuff):
    z_minVal = input_dict["z"]
    z_maxVal = 240
    shifted_joy_minVal = 0
    shifted_joy_maxVal = 2
    
    pos_z = ((((z_maxVal - z_minVal) / (shifted_joy_maxVal -shifted_joy_minVal)) * jbuff["axis_R2"]) + z_minVal) - z_minVal
    return pos_z
    


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