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
from IK import IK_in


""" VARIABLE DECLARATIONS """
modeVal = {"mode": 0, "prev_mode": 0 }
flags = {"position_reached": False, "return_to_Ready": False, "flag_thumbJoyStateChng_lx": False, "flag_thumbJoyStateChng_ly": False, "flag_thumbJoyStateChng_rx": False, "flag_thumbJoyStateChng_ry": False,}
JoyBuffer = {"left_x": 0.0, "left_y": 0.0, "right_x": 0.0, "right_y": 0.0}
AxisBuffer ={
				"axis_lx": 0.0, "axis_ly": 0.0, "axis_rx": 0.0, "axis_ry": 0.0, 
				"prev_axis_lx": 0.0 , "prev_axis_ly": 0.0, "prev_axis_rx": 0.0, "prev_axis_ry": 0.0,
				"lx_center": False, "ly_center": False, "rx_center": False, "ry_center": False
				
			}
auxVal = {"dist_to_grnd": 160.0}

EVENT = None


	
def JoyButtonHandler(event):
	#print "DIAG: EVENT = JoyButtonHandler"
	for i in range(funct.ds4.get_numbuttons()):
		btn_ID = funct.ds4.get_button(i)							
		if btn_ID == 1:															# a button was pushed
			if i == 0: 
				event = "SQUARE"
			elif i == 1: 
				event = "CROSS"
			elif i == 2: 
				event = "CIRCLE"
			elif i == 3: 
				event = "TRIANGLE"
			elif i == 4: 
				event = "L1"
			elif i == 5: 
				event = "R1"
				EventDispatch(event, modeVal, IK_in, AxisBuffer, flags)
			elif i == 6: 
				event = "L2"
			elif i == 7: 
				event = "R2"
				EventDispatch(event, modeVal, IK_in, AxisBuffer, flags)
			elif i == 8: 
				event = "SHARE"
			elif i == 9: 
				event = "OPTIONS"
				EventDispatch(event, modeVal, IK_in, AxisBuffer, flags)
			elif i == 10: 
				event = "LEFT THUMB. BTN."
			elif i == 11: 
				event = "RIGHT THUMB. BTN."
			elif i == 12: 
				event = "PSBTN"
				EventDispatch(event, modeVal, IK_in, AxisBuffer, flags)
			elif i == 13: 
				event = "TOUCH SCREEN"
	
	
def ThumbJoyHandler(jbuff, axisbuff, flag_dict, event):
	axisbuff["axis_lx"] = funct.ds4.get_axis(0)	* -1								# Bal oldali thumbjoy az x és y tengel menti forgásokat adja
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

	axisbuff["axis_rx"] = funct.ds4.get_axis(2)	* -1	
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
	

	if flag_dict["flag_thumbJoyStateChng_lx"] or flag_dict["flag_thumbJoyStateChng_ly"] or flag_dict["flag_thumbJoyStateChng_rx"] or flag_dict["flag_thumbJoyStateChng_ry"] == True:
		event = "THMB_JOY"
		print "THMB_JOYEVENT ---> THMB_JOYEVENT"
		EventDispatch(event, modeVal, IK_in, JoyBuffer, flags)
		flag_dict["flag_thumbJoyStateChng"] = False
	
	
	
def EventSource():
	for event in funct.pygame.event.get():
		if event.type == funct.pygame.JOYBUTTONDOWN:
			JoyButtonHandler(EVENT)
			
		elif event.type == funct.pygame.JOYHATMOTION:           
			pass
			
		elif event.type == funct.pygame.JOYAXISMOTION:
			ThumbJoyHandler(JoyBuffer, AxisBuffer, flags, EVENT)
	
	
def EventDispatch(event, mode_dict, direction_dict, jbuff, flag_dict):
	if (event == "OPTIONS"):                      		  						# HA az OPTIONS gombot megnyomtak,
		print "MAIN: Changing mode..."
		mode_dict["prev_mode"] = mode_dict["mode"]
		if mode_dict["prev_mode"] == 3:
			flag_dict["return_to_Ready"] = True
			
		mode_dict["mode"] = mode_dict["mode"] + 1          						# akkor a mode valtozot noveljuk
		if mode_dict["mode"] == 4:                     							# HA mode = 4 (ilyen mode nincs), akkor
			print "MAIN: Returning to READY..."
			mode_dict["mode"] = 1                      							# menjunk vissza READY mode-ba
			
		event = ""                                  							# EVENT valtozo torlese
		print "MAIN_ mode is: " + str(mode_dict["mode"])
		flag_dict["position_reached"] = False
		
	elif (event == "PSBTN"):                    	    						# HA a PS gombot megnyomtak, akkor
		if mode_dict["mode"] == 1:
			print "MAIN: Returning to IDLE..."
			mode_dict["mode"] = 0
			event = ""
			flag_dict["position_reached"] = False
		else:
			print "MAIN: Returning to READY..."
			mode_dict["mode"] == 1
			flag_dict["return_to_Ready"] = True
			event = ""                      	            					# végül a EVENT változót töröljük
			flag_dict["position_reached"] = False

	elif event == "THMB_JOY":
		if mode_dict["mode"] == 2:
			direction_dict["ROT_X"] = 10 * jbuff["left_y"]
			direction_dict["ROT_Y"] = 10 * jbuff["left_x"] 
			direction_dict["POS_X"] = 50 * jbuff["right_x"] 
			direction_dict["POS_Y"] = 50 * jbuff["right_y"]
			flag_dict["position_reached"] = False
				
	elif (event == "R1"):														# Függőleges emelkedes Z tengely menten 10mm lepesekben
		if mode_dict["mode"] == 2:
			if auxVal["dist_to_grnd"] < 240:
				direction_dict["POS_Z"] = direction_dict["POS_Z"] + 10
				auxVal["dist_to_grnd"] = auxVal["dist_to_grnd"] + 10
				print auxVal["dist_to_grnd"]
				flag_dict["position_reached"] = False
			else:
				print "DIAG: POS_Z max value reached!"
				
	elif (event == "R2"):														# Függőleges ereszkedes Z tengely menten 10mm lepesekben
		if mode_dict["mode"] == 2:			
			if auxVal["dist_to_grnd"] > 120:
				direction_dict["POS_Z"] = direction_dict["POS_Z"] - 10
				auxVal["dist_to_grnd"] = auxVal["dist_to_grnd"] - 10
				print auxVal["dist_to_grnd"]
				flag_dict["position_reached"] = False
			else:
				print "DIAG: POS_Z min value reached!"
			
"""			
	elif (event == "R1"):														# Függőleges emelkedes Z tengely menten 10mm lepesekben
		if mode_dict["mode"] == 2:
			direction_dict["POS_Z"] = direction_dict["POS_Z"] + 10
			if direction_dict["POS_Z"] >= 240:
				direction_dict["POS_Z"] = 240
				print "POS_Z max value reached!"
				flag_dict["position_reached"] = False
			flag_dict["position_reached"] = False
		
	elif (event == "R2"):														# Függőleges ereszkedes Z tengely menten 10mm lepesekben
		if mode_dict["mode"] == 2:
			direction_dict["POS_Z"] = direction_dict["POS_Z"] - 10
			if direction_dict["POS_Z"] <= 30:
				direction_dict["POS_Z"] = 30
				print "POS_Z min value reached!"
				flag_dict["position_reached"] = False
			flag_dict["position_reached"] = False
"""

def EventExecute(event, mode_dict, flag_dict):
	if mode_dict["mode"] == 0: # IDLE
		if flag_dict["position_reached"] == False:
			print "MAIN: MODE set to IDLE"              						# ide még a fejet idle-be parancsot be kell szúrni
			kematox.SetUpIdle()                        							# Kezdo, leultetett allapot felvetele
			print "MAIN: IDLE position reached\n"
			flag_dict["position_reached"] = True
			
		elif flag_dict["position_reached"] == True:
			pass
			
	elif mode_dict["mode"] == 1: # READY
		if flag_dict["position_reached"] == False:
			if flag_dict["return_to_Ready"] == True:
				print "MAIN: Retruning to READY"
				kematox.return_to_Ready()
				IK_in["POS_Z"] = 0.0
				print "MAIN: READY position reached\n"
				flag_dict["return_to_Ready"] = False
				flag_dict["position_reached"] = True
				
			elif flag_dict["return_to_Ready"] == False:
				print "MAIN: MODE set to READY"
				kematox.go_to_Ready()
				print "MAIN: READY position reached\n"
				flag_dict["position_reached"] = True
				
		elif flag_dict["position_reached"] == True:
			pass
			
	elif mode_dict["mode"] == 2: # STATIC
		if flag_dict["position_reached"] == False:
			IK.IK_SixLeg()
			kematox.use_IK_calc()
			#IK.IK_Diag(IK.IK_out)
			flag_dict["position_reached"] = True
			print "DIAG: MOVEMENT READY"
		elif flag_dict["position_reached"] == True:
			pass
		
	elif mode_dict["mode"] == 3: # WALK
		print "MAIN: MODE set to WALK"
		
	
""" PROGRAM START """	
kematox = obj.Hexapod("kematox")
funct.InitDS4()
funct.LookForDevices(kematox) 

while (True):
    try:
		EventSource()
		EventExecute(EVENT, modeVal, flags)
		
    except KeyboardInterrupt:
        funct.StopPrg(kematox)
        
    
    
