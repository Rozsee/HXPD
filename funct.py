# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 21:27:17 2018

@author: Rozsee
"""
import pygame
import sys

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