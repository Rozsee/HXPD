# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 21:29:41 2018

@author: Rozsee
"""
import serial  
#from copy import deepcopy
#import RPi.GPIO as GPIO                                                      # GPIO-t kezelő modul importálása
#GPIO.setmode(GPIO.BCM)        
import pos
#import IK
from IK import IK_in, IK_out, TripodA_MoveTable, TripodB_MoveTable

#walkVal = {"tripod_substep": 0, "walkmode": "TRIPOD", "def_tripod_step_1_complete": False, "def_tripod_step_2_complete": False}

"""CLASSES..."""
class Servo:
    def __init__(self, Servo_Id, Servo_Pos, SrvCtrl):                         # Minden létrehozott szervo példánynak legyen
        self.ID = Servo_Id                                                   # egy azonosítója (a leg-től kapja)
        self.Position = Servo_Pos                                             # egy pozicio értéke ms-ben (a leg-től kapja)
        self.SrvCtrl = SrvCtrl

    def SetServoPosition(self):
        """Egy láb tetszőleges szervóját mozgatja."""
        self.SrvCtrl.SetToMove("#" + str(self.ID) + "P" + str(self.Position)) 
        #print "SetServoPosition lefutott..."
    
                                                        
class Leg:
    def __init__(self, servo_param_dict, SrvCtrl):                            # Létrehozzuk a lához tartozó szervó példányokat
        self.Name = servo_param_dict.get("name")
        self.Coxa = Servo(servo_param_dict.get("id_coxa"), servo_param_dict.get("pos_coxa"), SrvCtrl)
        self.Femur = Servo(servo_param_dict.get("id_femur"), servo_param_dict.get("pos_femur"), SrvCtrl)
        self.Tibia = Servo(servo_param_dict.get("id_tibia"), servo_param_dict.get("pos_tibia"), SrvCtrl)
#        GPIO.setup(servo_param_dict.get("GPIO"), GPIO.IN)                    # Setup footswitch GPIO port to IN
        self.FootSwitch = servo_param_dict.get("GPIO")
    
    def updatePosition(self, posDict):
        self.Coxa.Position = posDict["pos_coxa"]
        #print self.Coxa.Position
        self.Femur.Position = posDict["pos_femur"]
        #print self.Femur.Position
        self.Tibia.Position = posDict["pos_tibia"]
        #print self.Tibia.Position

    def SetLegPosition(self):
        Servo.SetServoPosition(self.Coxa)
        Servo.SetServoPosition(self.Femur)
        Servo.SetServoPosition(self.Tibia)
        #print "SetLegPosition lefutott..."


class Head:        
    def __init__(self, servo_param_dict, SrvCtrl):
        self.Name = servo_param_dict.get("name")
        self.HeadRot = Servo(servo_param_dict.get("id_head_rot"), servo_param_dict.get("pos_head_rot"), SrvCtrl)
    
    def updatePosition(self, posDict):
        self.HeadRot.Position = posDict["pos_head_rot"]
    
    def SetHeadPosition(self):
        Servo.SetServoPosition(self.HeadRot)

        
        
class SrvCtrl(object):
    """ Szervo kontroller objektum. A SSC32 számára állítja össze a parancs sztringet és 
    küldi ki azt a soros porton."""
    Name = None
    CmdBuf = None
    Port = None

    def __init__(self, name):
        self.Name = name
        self.CmdBuf = ""
        self.Port = serial.Serial('COM3', 115200, timeout = 0.06)              # LINUXHOZ: serial.Serial('/dev/ttyAMA0', 115200, timeout = 1) comport was 3

    def SetToMove(self, cmd_string):
        """ A paraméterként megadott stringet mindíg hozzáadjuk a CmdBuf-hoz """
        self.CmdBuf = self.CmdBuf + cmd_string
    """def ExecuteMove(self, MoveTime):
        defMoveTime = 750
        if MoveTime == None:
            self.CmdBuf = self.CmdBuf + "T" + str(defMoveTime) + "\r\n"
            print "SRVCTRL in: " + self.CmdBuf
            self.Port.write(self.CmdBuf)
            while True:
                self.Port = "Q\r\n"
                resp = self.Port.readline()
                print "SRVCTRL out: " + resp
                if resp == ".":
                    break
            self.CmdBuf = ""
        else:
            self.CmdBuf = self.CmdBuf + "T" + str(MoveTime) + "\r\n"
            self.Port.write(self.CmdBuf)
            print "SRVCTRL in: " + self.CmdBuf
            while True:
                self.Port.write("Q\r\n")
                resp = self.Port.readline()
                print "SRVCTRL out: " + resp
                if resp == ".":
                    break
            self.CmdBuf = ""
"""
    def ExecuteMove(self, MoveTime, querry):
        """ ExecuteMove-al adjuk hozzá a CmdBuf-hoz a mozgatási időt (le-
        zárva a parancs szringet) és küldjük ki soros porton a  parancsot
        szervovezérlőnek ezzel indítva a mozgás végrehajtását """
        defMoveTime = 750                                               # was 750 
        if MoveTime == None:
            self.CmdBuf = self.CmdBuf + "T" + str(defMoveTime) + "\r\n"
            #print "SRVCTRL in: " + self.CmdBuf
            self.Port.write(self.CmdBuf)
            if querry == "Poll":
                print "SSC32: Polling SRVCNTRL till movement finished... Using default movetime..."
                while True:
                    self.Port = "Q\r\n"
                    resp = self.Port.readline()
                    print "SRVCTRL out: " + resp
                    if resp == ".":
                        break
                self.CmdBuf = ""
            elif querry == "NoPoll":
                print "SSC32: Polling turned OFF! Using default movetime..."
                self.CmdBuf = ""
        else:
            self.CmdBuf = self.CmdBuf + "T" + str(MoveTime) + "\r\n"
            #print "SRVCTRL in: " + self.CmdBuf
            self.Port.write(self.CmdBuf)
            if querry == "Poll":
                print "SSC32: Polling SRVCNTRL movement finished... Using preset/calc. movetime"
                while True:
                    self.Port.write("Q\r\n")
                    resp = self.Port.readline()
                    print "SRVCTRL out: " + resp
                    if resp == ".":
                        break
                self.CmdBuf = ""     
            elif querry == "NoPoll":
                print "SSC32: Polling turned OFF! Using preset/calc. movetime."
                self.CmdBuf = ""


class Hexapod(object):
    servo_param_dict = None                                                  # ezek a osztályváltozók ide nem kötelezően kelenek. Működik e nélkül is,
    Name = None                                                              # az osztályváltozók felsorolása az osztály öröklésnél fontos
    RF = None
    RM = None
    RR = None
    LF = None
    LM = None
    LR = None
    HEAD = None
    SRVCTRL = None    
    
    def __init__(self, name):
        self.servo_param_dict = {
                "RF": {"name": "RF", "GPIO": 17, "pos_femur": None, "pos_tibia": None, "pos_coxa": None, "id_femur": 1, "id_tibia": 2, "id_coxa": 0, "chngd": 0},  # Right front leg (CON:2); femur = felsö labsz, tibia = also labsz.
                "RM": {"name": "RM", "GPIO": 27, "pos_femur": None, "pos_tibia": None, "pos_coxa": None, "id_femur": 9, "id_tibia":10, "id_coxa": 8, "chngd": 0},  # Right middle leg (CON:4)
                "RR": {"name": "RR", "GPIO": 22, "pos_femur": None, "pos_tibia": None, "pos_coxa": None, "id_femur": 5, "id_tibia": 6, "id_coxa": 4, "chngd": 0},  # Right rear leg (CON:6)
                "LF": {"name": "LF", "GPIO": 23, "pos_femur": None, "pos_tibia": None, "pos_coxa": None, "id_femur":17, "id_tibia":18, "id_coxa":16, "chngd": 0},  # Left front leg (CON:1)
                "LM": {"name": "LM", "GPIO": 24, "pos_femur": None, "pos_tibia": None, "pos_coxa": None, "id_femur":25, "id_tibia":26, "id_coxa":24, "chngd": 0},  # Left middle leg (CON:3)
                "LR": {"name": "LR", "GPIO": 25, "pos_femur": None, "pos_tibia": None, "pos_coxa": None, "id_femur":21, "id_tibia":22, "id_coxa":20, "chngd": 0},  # Left rear leg (CON:5)
                "HEAD": {"name": "HEAD", "pos_head_rot": 1500, "id_head_rot": 19, "chngd": 0}                                                                              # Dict. for Head parameters
                }                                                            # Az összes végtag paraméterét tartalmazo dict. Az egyes lábak külön dict-be rendezve a dict-en belül
        
        self.Name = name
        self.SRVCTRL = SrvCtrl("SSC32") 
        self.RF = Leg(self.servo_param_dict["RF"], self.SRVCTRL)             # Leg példányok létrehozása a param_dict dictonary megfelelő adataival A.) módon
        self.RM = Leg(self.servo_param_dict.get("RM"), self.SRVCTRL)         # Leg példányok létrehozása a param_dict dictonary megfelelő adataival B.) módon
        self.RR = Leg(self.servo_param_dict.get("RR"), self.SRVCTRL)         # többszintű dictonary kulcsainak és értékeinek elérése a get() funkcióval, vagy "manuálisan": outer_dictname[inner_dictname][inner_dictname_value]
        self.LF = Leg(self.servo_param_dict.get("LF"), self.SRVCTRL)
        self.LM = Leg(self.servo_param_dict.get("LM"), self.SRVCTRL)
        self.LR = Leg(self.servo_param_dict.get("LR"), self.SRVCTRL)
        self.HEAD = Head(self.servo_param_dict.get("HEAD"), self.SRVCTRL)
        #return self # csak az init után kell return self-et alkalmazni.        
        
    """def Update_Spdict(self, input_dict):
        if "RF" in input_dict:
           self.RF.updatePosition(input_dict["RF"])         # az aktuális lábhoz tartozo dict-et updtate-eljük az új szervo pozicókkal
        else:
            pass
        if "RM" in input_dict:
            self.RM.updatePosition(input_dict["RM"])
        else:
            pass
        if "RR" in input_dict:
            self.RR.updatePosition(input_dict["RR"])
        else:
            pass
        if "LF" in input_dict:
            self.LF.updatePosition(input_dict["LF"])
        else:
            pass
        if "LM" in input_dict:
            self.LM.updatePosition(input_dict["LM"])
        else:
            pass
        if "LR" in input_dict:
            self.LR.updatePosition(input_dict["LR"])
        else:
            pass
        self.SetLegsPosition()                          # Az új szervopozíciókkal feltöltjük a "láb" objektumokat és a végén legyártjuk a parancs stringet (SetToMove)
        self.SRVCTRL.ExecuteMove(250)                       # step végrehajtás. 1 step a megadott ido alatt hajtódik végre (ExcecuteMove) was 500ms


    def SetLegsPosition(self):
        self.RF.SetLegPosition()
        self.RM.SetLegPosition()
        self.RR.SetLegPosition()
        self.LF.SetLegPosition()
        self.LM.SetLegPosition()
        self.LR.SetLegPosition()
"""
    def Update_Spdict(self, input_dict, legs_select, leg_mode, steptime):
        """ Az egyes lábakhoz tartozó szervo poziciókat frissíti az új pozíció
        értékekkel, melyeket az input_dict[] tartalmaz. 
        FONTOS: nem a servo_param_dict-et
        frssitjük (mint ami az eredeti elképzelés volt, mert ugyan az objektumokat a
        servo_param_dict segítségével hoztuk létre, de ha modosúl a servo_param_dict
        dictonary, attol még az objektumokban az értékek nem frissülnek maguktól.
        Erre kell a Leg.updatePosition metódus"""
        if legs_select == "all":
            self.RF.updatePosition(input_dict["RF"])
            self.RM.updatePosition(input_dict["RM"])
            self.RR.updatePosition(input_dict["RR"])
            self.LF.updatePosition(input_dict["LF"])
            self.LM.updatePosition(input_dict["LM"])
            self.LR.updatePosition(input_dict["LR"])
            if leg_mode == "swing":
                self.SetLegsPosition("all")
                self.SRVCTRL.ExecuteMove(steptime, "Poll")
            elif leg_mode == "support":
                self.SetLegsPosition("all")
                self.SRVCTRL.ExecuteMove(steptime, "NoPoll")

        elif legs_select == "TripodA":
            self.RF.updatePosition(input_dict["RF"])
            self.LM.updatePosition(input_dict["LM"])
            self.RR.updatePosition(input_dict["RR"])
            if leg_mode == "swing":
                self.SetLegsPosition("TripodA")
                self.SRVCTRL.ExecuteMove(steptime, "Poll")
            elif leg_mode == "support":
                self.SetLegsPosition("TripodA")
                self.SRVCTRL.ExecuteMove(steptime, "NoPoll")

        elif legs_select == "TripodB":
            self.LF.updatePosition(input_dict["LF"])
            self.RM.updatePosition(input_dict["RM"])
            self.LR.updatePosition(input_dict["LR"])
            if leg_mode == "swing":
                self.SetLegsPosition("TripodB")
                self.SRVCTRL.ExecuteMove(steptime, "Poll")
            elif leg_mode == "support":
                self.SetLegsPosition("TripodB")
                self.SRVCTRL.ExecuteMove(steptime, "NoPoll")


    def SetLegsPosition(self, legs_select):
        """ Az egyes lábakat felépító szervo példányok pozicióját beállítja a 
        servo_param_dict-ben tárolt pozició adatok szerint és legyártja a 
        parancs stringet """
        if legs_select == "all":
            self.RF.SetLegPosition()
            self.RM.SetLegPosition()
            self.RR.SetLegPosition()
            self.LF.SetLegPosition()
            self.LM.SetLegPosition()
            self.LR.SetLegPosition()
            #print "SetLegsPosition - all lefutott" 

        elif legs_select == "TripodA":
            self.RF.SetLegPosition()
            self.LM.SetLegPosition()
            self.RR.SetLegPosition()

        elif legs_select == "TripodB":
            self.LF.SetLegPosition()
            self.RM.SetLegPosition()
            self.LR.SetLegPosition()        

    def MoveHead(self):
        #self.Update_Spdict()                                                # Ezen még dolgozni, kell, ha kitaláltam milyen bemenö dict-ben tárolom a fej mozgásához szükséges paramétereket
        self.Head.SetHeadPosition   
        self.SRVCTRL.ExecuteMove(None)  

    def SetUpIdle(self):
        self.Update_Spdict(pos.pos_idle["step_1"], "all", "support", 500)

    def return_to_Idle(self):
        """ READY pozícióból IDLE pozicíóba viszi a robotot """
        self.Update_Spdict(pos.rdy_to_idle["step_8"], "TripodA", "swing", 500) # TPB
        self.Update_Spdict(pos.rdy_to_idle["step_5"], "TripodA", "swing", 500) # TPB
        self.Update_Spdict(pos.rdy_to_idle["step_6"], "TripodB", "swing", 500) # TPA
        self.Update_Spdict(pos.rdy_to_idle["step_3"], "TripodB", "swing", 500) # TPA
        self.Update_Spdict(pos.rdy_to_idle["step_8"], "TripodA", "swing", 500)
        self.Update_Spdict(pos.rdy_to_idle["step_81"], "TripodA", "swing", 500)
        self.Update_Spdict(pos.rdy_to_idle["step_82"], "TripodB", "swing", 500)
        self.Update_Spdict(pos.rdy_to_idle["step_83"], "TripodB", "swing", 500)
        self.Update_Spdict(pos.rdy_to_idle["step_84"], "all", "swing", 1000)
        

    def go_to_Ready(self):
        """ IDLE pozícióból READY pozicíóba viszi a robotot """
        self.Update_Spdict(pos.idle_to_rdy["step_1"], "all", "swing", 500)
        self.Update_Spdict(pos.idle_to_rdy["step_2"], "TripodB", "swing", 500) # TPA
        self.Update_Spdict(pos.idle_to_rdy["step_3"], "TripodB", "swing", 500) # TPA
        self.Update_Spdict(pos.idle_to_rdy["step_4"], "TripodA", "swing", 500) # TPB
        self.Update_Spdict(pos.idle_to_rdy["step_5"], "TripodA", "swing", 500) # TPB
        self.Update_Spdict(pos.idle_to_rdy["step_6"], "TripodB", "swing", 500) # TPA
        self.Update_Spdict(pos.idle_to_rdy["step_7"], "TripodB", "swing", 500) # TPA
        self.Update_Spdict(pos.idle_to_rdy["step_8"], "TripodA", "swing", 500) # TPB
        self.Update_Spdict(pos.idle_to_rdy["step_9"], "TripodA", "swing", 500) # TPB

    def go_to_Ready_v2(self):
        """ IDLE pozícióból READY pozicíóba viszi a robotot """
        self.Update_Spdict(pos.idle_to_rdy_v2["step_1"], "all", "swing", 500)
        self.Update_Spdict(pos.idle_to_rdy_v2["step_2"], "TripodB", "swing", 500) # TPA
        self.Update_Spdict(pos.idle_to_rdy_v2["step_3"], "TripodB", "swing", 250) # TPA
        self.Update_Spdict(pos.idle_to_rdy_v2["step_4"], "TripodA", "swing", 500) # TPB
        self.Update_Spdict(pos.idle_to_rdy_v2["step_5"], "TripodA", "swing", 250) # TPB

    def return_to_Ready(self):
        """ Elvileg bármilyen pozícióbol READY pozícióba viszi a robotot """
        self.Update_Spdict(pos.ret_to_rdy["step_1"], "TripodB", "swing", 500)
        self.Update_Spdict(pos.ret_to_rdy["step_2"], "TripodB", "swing", 500)
        self.Update_Spdict(pos.ret_to_rdy["step_3"], "TripodA", "swing", 500)
        self.Update_Spdict(pos.ret_to_rdy["step_4"], "TripodA", "swing", 500)
    

    def use_IK_calc(self):
        self.Update_Spdict(IK_out, "all", "support", 500)                         # time was 750ms, mode was swing -> each new position was waited to be executed 

    
    def go_to_Trans_I(self):
        self.Update_Spdict(pos.rdy_to_trns_1["step_1"])
        self.Update_Spdict(pos.rdy_to_trns_1["step_2"])
        self.Update_Spdict(pos.rdy_to_trns_1["step_3"])
        self.Update_Spdict(pos.rdy_to_trns_1["step_4"])
        self.Update_Spdict(pos.rdy_to_trns_1["step_5"])
    
    def MoveTripodA(self, gate, mode, StepTime):
        if gate == "default":
            if mode == "support":
                self.Update_Spdict(TripodA_MoveTable, "TripodA", "support", StepTime)
            elif mode == "swing":
                print "Most emelem A-t!"
                self.Update_Spdict(TripodA_MoveTable, "TripodA", "swing", StepTime / 2)
        elif gate == "wave":
            pass


    def MoveTripodB(self, gate, mode, StepTime):
        if gate == "default":
            if mode == "support":
                print "Most tartom B-t!"
                self.Update_Spdict(TripodB_MoveTable, "TripodB", "support", StepTime)
            elif mode == "swing":
                print "Most emelem B-t!"
                self.Update_Spdict(TripodB_MoveTable, "TripodB", "swing", StepTime / 2)
        elif gate == "wave":
            pass



    """
    def Def_TRIPOD_Step_1(walk_val):
        
        IK_Tripod_A("support")
        self.Update_Spdict(TripodA_MoveTable, "TripodA", "support", StepTime)
        
        global IK_in_for_Swing
     
        ModifyIKinForSwingLeg(IK_in, IK_in_for_Swing, auxVal, "up")               # ADD x to z_offset distance to lift legs 
        IK_Tripod_B("swing")
        self.Update_Spdict(TripodB_MoveTable, "TripodB", "swing", StepTime / 2)
        print "TRPD B UP"

        IK.ModifyIKinForSwingLeg(IK_in, IK_in_for_Swing, auxVal, "down")          # SUBTRACT x from z_offset distance to lower legs
        IK_Tripod_B("swing")
        self.Update_Spdict(TripodB_MoveTable, "TripodB", "swing", StepTime / 2)
        print "TRPD B DOWN"

        IK_in_for_Swing = dict.fromkeys(IK_in_for_Swing, 0)
        
        walk_val["def_tripod_step_1_complete"] = True
        walk_val["def_tripod_step_2_complete"] = False
        """
    
    """
    def Walk_def_TRIPOD(self, walk_val):
        #StepTime = int(round(IK.CalcStepTime(WalkVector)))                        # a legkozelebbi integerre kerekitjuk a steptime valtozot
        StepTime = 750        
        if walk_val["tripod_substep"] == 0:
            print "LEPES CIKLUS START!"
            IK_Tripod_A("support")
            self.Update_Spdict(TripodA_MoveTable, "TripodA", "support", StepTime)
            
                         
            ModifyIKinForSwingLeg(IK_in, auxVal, "up", IK_in_for_Swing)                  # ADD x to z_offset distance to lift legs 
            print IK_in_for_Swing
            
            IK_Tripod_B("swing")
            self.Update_Spdict(TripodB_MoveTable, "TripodB", "swing", StepTime / 2)
            print "TRPD B UP"
            
       

            IK.ModifyIKinForSwingLeg(IK_in, auxVal, "down", IK_in_for_Swing)                # SUBTRACT x from z_offset distance to lower legs
            print "IK for swing:"
            print IK_in_for_Swing
            
            self.Update_Spdict(TripodB_MoveTable, "TripodB", "swing", StepTime / 2)
            print "TRPD B DOWN"
            
           
         #   IK_in_for_Swing = dict.fromkeys(IK_in_for_Swing, 0)
            
            walk_val["tripod_substep"] = 1

        elif walk_val["tripod_substep"] == 1:
            IK_Tripod_B("support")
            self.Update_Spdict(TripodB_MoveTable, "TripodB", "support", StepTime)   

            ModifyIKinForSwingLeg(IK_in, IK_in_for_Swing, auxVal, "up")                  # ADD x to z_offset distance to lift legs
            IK_Tripod_A("swing")
            self.Update_Spdict(TripodA_MoveTable, "TripodA", "swing", StepTime / 2)
            print "TRPD A UP"

            ModifyIKinForSwingLeg(IK_in, IK_in_for_Swing, auxVal, "down")                #SUBTRACT x from z_offset distance to lower legs
            IK_Tripod_A("swing")
            self.Update_Spdict(TripodA_MoveTable, "TripodA", "swing", StepTime / 2)
            print "TRPD A DOWN"

            IK_in_for_Swing = dict.fromkeys(IK_in_for_Swing, 0)

            walk_val["tripod_substep"] = 0
            print "LEPES CIKLUS END!"
    """
    """
    def LegFeetToGround(self, leg):
        pass
    
    def TripodFeetToGround(self, tripod):
        pass
    """