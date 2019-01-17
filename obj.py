# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 21:29:41 2018

@author: Rozsee
"""
import serial  
#import RPi.GPIO as GPIO                                                      # GPIO-t kezelő modul importálása
#GPIO.setmode(GPIO.BCM)        
import pos
from IK_funct import IK_out


"""CLASSES..."""
class Servo:
    def __init__(self, Servo_Id, Servo_Pos, SrvCtrl):                         # Minden létrehozott szervo példánynak legyen
        self.ID	= Servo_Id                                                   # egy azonosítója (a leg-től kapja)
        self.Position = Servo_Pos                                             # egy pozicio értéke ms-ben (a leg-től kapja)
        self.SrvCtrl = SrvCtrl

    def SetServoPosition(self):
        """Egy láb tetszőleges szervóját mozgatja."""
        self.SrvCtrl.SetToMove("#" + str(self.ID) + "P" + str(self.Position)) 
    
                                                        
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
        self.Femur.Position = posDict["pos_femur"]
        self.Tibia.Position = posDict["pos_tibia"]

    def SetLegPosition(self):
        Servo.SetServoPosition(self.Coxa)
        Servo.SetServoPosition(self.Femur)
        Servo.SetServoPosition(self.Tibia)


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
        
    def ExecuteMove(self, MoveTime):
        """ ExecuteMove-al adjuk hozzá a CmdBuf-hoz a mozgatási időt (le-
        zárva a parancs szringet) és küldjük ki soros porton a  parancsot
        szervovezérlőnek ezzel indítva a mozgás végrehajtását """
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
	class Tripod:
	Name = None
	Leg_1 = None
	Leg_2 = None
	Leg_3 = None
	Move_Delay = None
	
	def __init__(self, name, leg_1, leg_2, leg_3, move_delay):
		self.Name = name
		self.Leg_1 = leg_1
		self.Leg_2 = leg_2
		self.Leg_3 = leg_3
		self.Move_Delay = move_delay
		
	def TripodMove(self, ):
		pass
"""
            
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
        
        """
        self.TRIPOD_1 = [self.RF, self.RR, self.LM]
        self.TRIPOD_2 = [self.LF, self.LR, self.RM]
        """
        
        
                   
    def Update_Spdict(self, input_dict):
        """ Az egyes lábakhoz tartozó szervo poziciókat frissíti az új pozíció
        értékekkel, melyeket az input_dict[] tartalmaz. 
        FONTOS: nem a servo_param_dict-et
        frssitjük (mint ami az eredeti elképzelés volt, mert ugyna az objektumokat a
        servo_param_dict segítségével hoztuk létre, de ha modosúl a servo_param_dict
        dictonary, attol még az objektumokban az értékek nem frissülnek maguktól.
        Erre kell a Leg.updatePosition metódus"""
        if "RF" in input_dict:
           self.RF.updatePosition(input_dict["RF"])                             # az aktuális lábhoz tartozo dict-et updtate-eljük az új szervo pozicókkal
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
        self.SetLegsPosition()                                               # Az új szervopozíciókkal feltöltjük a "láb" objektumokat és a végén legyártjuk a parancs stringet (SetToMove)
        self.SRVCTRL.ExecuteMove(250)                                       # step végrehajtás. 1 step a megadott ido alatt hajtódik végre (ExcecuteMove) was 500ms


    def SetLegsPosition(self):
        """ Az egyes lábakat felépító szervo példányok pozicióját beállítja a 
        servo_param_dict-ben tárolt pozició adatok szerint és legyártja a 
        parancs stringet """
        self.RF.SetLegPosition()
        self.RM.SetLegPosition()
        self.RR.SetLegPosition()
        self.LF.SetLegPosition()
        self.LM.SetLegPosition()
        self.LR.SetLegPosition()
        

    def MoveHead(self):
        #self.Update_Spdict()                                                # Ezen még dolgozni, kell, ha kitaláltam milyen bemenö dict-ben tárolom a fej mozgásához szükséges paramétereket
        self.Head.SetHeadPosition   
        self.SRVCTRL.ExecuteMove(None)  
        

    def SetUpIdle(self):
        self.Update_Spdict(pos.pos_idle["step_1"])
        

    def return_to_Idle(self):
        """ READY pozícióból IDLE pozicíóba viszi a robotot """
        self.Update_Spdict(pos.rdy_to_idle["step_1"])
        self.Update_Spdict(pos.rdy_to_idle["step_2"])
        self.Update_Spdict(pos.rdy_to_idle["step_3"])
        self.Update_Spdict(pos.rdy_to_idle["step_4"])
        self.Update_Spdict(pos.rdy_to_idle["step_5"])
        self.Update_Spdict(pos.rdy_to_idle["step_6"])
        self.Update_Spdict(pos.rdy_to_idle["step_7"])
        self.Update_Spdict(pos.rdy_to_idle["step_8"])


    def go_to_Ready(self):
        """ IDLE pozícióból READY pozicíóba viszi a robotot """
        self.Update_Spdict(pos.idle_to_rdy["step_1"])
        self.Update_Spdict(pos.idle_to_rdy["step_2"])
        self.Update_Spdict(pos.idle_to_rdy["step_3"])
        self.Update_Spdict(pos.idle_to_rdy["step_4"])
        self.Update_Spdict(pos.idle_to_rdy["step_5"])
        self.Update_Spdict(pos.idle_to_rdy["step_6"])
        self.Update_Spdict(pos.idle_to_rdy["step_7"])
        self.Update_Spdict(pos.idle_to_rdy["step_8"])
        self.Update_Spdict(pos.idle_to_rdy["step_9"])
    

    def return_to_Ready(self):
        """ Elvileg bármilyen pozícióbol READY pozícióba viszi a robotot.
        Azért ezt még tesztelni kell... """
        self.Update_Spdict(pos.reset_tripod_1["step_1"])
        self.Update_Spdict(pos.reset_tripod_1["step_2"])
        self.Update_Spdict(pos.reset_tripod_2["step_1"])
        self.Update_Spdict(pos.reset_tripod_2["step_2"])
    

    def use_IK_calc(self):
        self.Update_Spdict(IK_out)	

    
    def go_to_Trans_I(self):
        self.Update_Spdict(pos.rdy_to_trns_1["step_1"])
        self.Update_Spdict(pos.rdy_to_trns_1["step_2"])
        self.Update_Spdict(pos.rdy_to_trns_1["step_3"])
        self.Update_Spdict(pos.rdy_to_trns_1["step_4"])
        self.Update_Spdict(pos.rdy_to_trns_1["step_5"])
    
    """def return_from_Trans_I(self):
        pass"""
    
    def Walk(self):
        pass
    
    def Rotate(self):
        pass
    
    def Translate(self):
        pass
    
    def Mixed(self):
        pass
    
    
    
    def LegFeetToGround(self, leg):
        pass
    
    def TripodFeetToGround(self, tripod):
        pass