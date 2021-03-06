# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 21:04:10 2018

@author: Rozsee
"""
pos_idle = {"step_1": {
                        #"RF": {"pos_femur": 2450, "pos_tibia": 1800, "pos_coxa": 2060}, # pos_coxa was 2060
                        "RF": {"pos_femur":  550, "pos_tibia": 1200, "pos_coxa": 2060}, # RF tibia and femur servos were replaced to JX ó. It is rotating opposit as Hitec
                        "RM": {"pos_femur": 2450, "pos_tibia": 1800, "pos_coxa": 1500},
                        "RR": {"pos_femur": 2450, "pos_tibia": 1800, "pos_coxa":  940},
                        #"LF": {"pos_femur":  550, "pos_tibia": 1150, "pos_coxa":  940},
                        "LF": {"pos_femur":  2450, "pos_tibia": 1850, "pos_coxa":  940},
                        "LM": {"pos_femur":  550, "pos_tibia": 1150, "pos_coxa": 1500},
                        "LR": {"pos_femur":  550, "pos_tibia": 1150, "pos_coxa": 2060}
                      }
            }

idle_to_rdy = {
            "step_1": {# FELÁLL
                        #"RF": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa": 2060},
                        "RF": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 2060}, #Femur & Tibia servo change (JX)!
                        "RM": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa":  940},
                        #"LF": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa":  940},
                        "LF": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa":  940},
                        "LM": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 2060}
                      },
            "step_2": {# 1 TRIPOD LÁBAKAT EMEL
                        #"RF": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa": 2060},
                        "RF": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 2060},
                        "RM": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa":  940},
                        #"LF": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa":  940},
                        "LF": {"pos_femur":  2400, "pos_tibia": 2000, "pos_coxa":  940},
                        "LM": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 1500},
                        "LR": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 2060}
                      },
            "step_3": {# 1 TRIPOD LÁBAKAT LERAK
                        #"RF": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa": 2060},
                        "RF": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 2060},
                        "RM": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa":  940},
                        #"LF": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa":  940},
                        "LF": {"pos_femur": 1737, "pos_tibia": 1747, "pos_coxa":  940},
                        "LM": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 2060}
                      },
            "step_4": {# 2 TRIPOD LÁBAKAT EMEL
                        #"RF": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 2060},
                        "RF": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 2060},
                        "RM": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1500},
                        "RR": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa":  940},
                        #"LF": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa":  940},
                        "LF": {"pos_femur": 1737, "pos_tibia": 1747, "pos_coxa":  940},
                        "LM": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 2060}
                      },
            "step_5": {# 2 TRIPOD LÁBAKAT LERAK
                        #"RF": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 2060},
                        "RF": {"pos_femur": 1253, "pos_tibia": 1253, "pos_coxa": 2060},
                        "RM": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa":  940},
                        #"LF": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa":  940},
                        "LF": {"pos_femur": 1737, "pos_tibia": 1747, "pos_coxa":  940},
                        "LM": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 2060}
                      },
            "step_6": {# 1 TRIPOD LÁBAKAT EMEL, CSÍPŐKET VÉGLEGES POZICIÓBA HOZ
                        #"RF": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 2060},
                        "RF": {"pos_femur": 1253, "pos_tibia": 1253, "pos_coxa": 2060},
                        "RM": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa":  940},
                        #"LF": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1355},
                        "LF": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1355},
                        "LM": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1500},
                        "LR": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1644}
                      },
            "step_7": {# 1 TRIPOD LÁBAKAT LERAK
                        #"RF": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 2060},
                        "RF": {"pos_femur": 1253, "pos_tibia": 1253, "pos_coxa": 2060},
                        "RM": {"pos_femur": 1738, "pos_tibia": 1731, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa":  940},
                        #"LF": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1355},
                        "LF": {"pos_femur": 1729, "pos_tibia": 1792, "pos_coxa": 1355},
                        "LM": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1644}
                      },
            "step_8": {# 2 TRIPOD LÁBAKAT EMEL, CSÍPŐKET VÉGLEGES POZICIÓBA HOZ
                        #"RF": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1644},
                        "RF": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1644},
                        "RM": {"pos_femur": 1738, "pos_tibia": 1731, "pos_coxa": 1500},
                        "RR": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1356},
                        #"LF": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1355},
                        "LF": {"pos_femur": 1729, "pos_tibia": 1792, "pos_coxa": 1355},
                        "LM": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1644}
                      },
            "step_9": {# 2 TRIPOD LÁBAKAT LERAK
                        #"RF": {"pos_femur": 1729, "pos_tibia": 1792, "pos_coxa": 1644},
                        "RF": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1644},
                        "RM": {"pos_femur": 1738, "pos_tibia": 1731, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1729, "pos_tibia": 1792, "pos_coxa": 1356},
                        #"LF": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1355},
                        "LF": {"pos_femur": 1729, "pos_tibia": 1792, "pos_coxa": 1355},
                        "LM": {"pos_femur": 1262, "pos_tibia": 1269, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1644}
                      }
              }


idle_to_rdy_v2 = {
            "step_1": {# FELÁLL, D=291, z=55, Coxa servos of the front and rear legs are still in the idle position
                        "RF": {"pos_femur": 1127, "pos_tibia": 1527, "pos_coxa": 2060},
                        "RM": {"pos_femur": 2032, "pos_tibia": 1723, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1873, "pos_tibia": 1473, "pos_coxa":  940},
                        "LF": {"pos_femur": 1873, "pos_tibia": 1473, "pos_coxa":  940},
                        "LM": {"pos_femur":  968, "pos_tibia": 1277, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1127, "pos_tibia": 1527, "pos_coxa": 2060}
                      },
                      
            "step_2": {# FELÁLL, TRIPOD_B LÁBAKAT EMEL (RM, LF, LR)
                        "RF": {"pos_femur": 1127, "pos_tibia": 1527, "pos_coxa": 2060},
                        "RM": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1873, "pos_tibia": 1473, "pos_coxa":  940},
                        "LF": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa":  940},
                        "LM": {"pos_femur":  968, "pos_tibia": 1277, "pos_coxa": 1500},
                        "LR": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 2060}
                      },          
                      
            "step_3": {# FELÁLL, TRIPOD_B LÁBAKAT LERAK (RM, LF, LR): D=260, z=110)
                        "RF": {"pos_femur": 1127, "pos_tibia": 1527, "pos_coxa": 2060},
                        "RM": {"pos_femur": 2158, "pos_tibia": 1920, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1873, "pos_tibia": 1473, "pos_coxa":  940},
                        "LF": {"pos_femur": 2235, "pos_tibia": 2040, "pos_coxa":  940},#c1356
                        "LM": {"pos_femur":  968, "pos_tibia": 1277, "pos_coxa": 1500},
                        "LR": {"pos_femur":  765, "pos_tibia":  960, "pos_coxa": 2060} #c1644
                      },       
            
            "step_4": {# FELÁLL, TRIPOD_A LÁBAKAT EMEL (RF, RR, LM)
                        "RF": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 2060},
                        "RM": {"pos_femur": 2158, "pos_tibia": 1920, "pos_coxa": 1500},
                        "RR": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa":  940},
                        "LF": {"pos_femur": 2235, "pos_tibia": 2040, "pos_coxa":  940},
                        "LM": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1500},
                        "LR": {"pos_femur":  765, "pos_tibia":  960, "pos_coxa": 2060}
                      },         
                      
            "step_5": {# FELÁLL, TRIPOD_A LÁBAKAT LERAK (RF, RR, LM): D=260, z=110)
                        "RF": {"pos_femur":  765, "pos_tibia":  960, "pos_coxa": 2060},#c1644
                        "RM": {"pos_femur": 2158, "pos_tibia": 1920, "pos_coxa": 1500},
                        "RR": {"pos_femur": 2235, "pos_tibia": 2040, "pos_coxa":  940},#c1356
                        "LF": {"pos_femur": 2235, "pos_tibia": 2040, "pos_coxa":  940},
                        "LM": {"pos_femur":  842, "pos_tibia": 1080, "pos_coxa": 1500},
                        "LR": {"pos_femur":  765, "pos_tibia":  960, "pos_coxa": 2060}
                      }       
                  }

rdy_to_idle = {
            "step_1": {# FELÁLL
                        #"RF": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa": 2060},
                        "RF": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 2060},
                        "RM": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa":  940},
                        #"LF": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa":  940},
                        "LF": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa":  940},
                        "LM": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 2060}
                      },
            
            "step_3": {# 1 TRIPOD LÁBAKAT LERAK
                        #"RF": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa": 2060},
                        "RF": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 2060},
                        "RM": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa":  940},
                        #"LF": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa":  940},
                        "LF": {"pos_femur": 1737, "pos_tibia": 1747, "pos_coxa":  940},
                        "LM": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 2060}
                      },
            
            "step_5": {# 2 TRIPOD LÁBAKAT LERAK
                        #"RF": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 2060},
                        "RF": {"pos_femur": 1253, "pos_tibia": 1253, "pos_coxa": 2060},
                        "RM": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa":  940},
                        #"LF": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa":  940},
                        "LF": {"pos_femur": 1737, "pos_tibia": 1747, "pos_coxa":  940},
                        "LM": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 2060}
                      },
            "step_6": {# 1 TRIPOD LÁBAKAT EMEL, CSÍPŐKET VÉGLEGES POZICIÓBA HOZ
                        #"RF": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 2060},
                        "RF": {"pos_femur": 1253, "pos_tibia": 1253, "pos_coxa": 2060},
                        "RM": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa":  940},
                        #"LF": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1355},
                        "LF": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1355},
                        "LM": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1500},
                        "LR": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1644}
                      },
           
            "step_8": {# 2 TRIPOD LÁBAKAT EMEL, CSÍPŐKET VÉGLEGES POZICIÓBA HOZ
                        #"RF": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 2060}, # 1644
                        "RF": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 2060}, # 1644
                        "RM": {"pos_femur": 1738, "pos_tibia": 1731, "pos_coxa": 1500}, 
                        "RR": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa":  940}, # 1356
                        #"LF": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1355}, 
                        "LF": {"pos_femur": 1729, "pos_tibia": 1792, "pos_coxa": 1355},
                        "LM": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1500}, # 1500
                        "LR": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1644}   
                      },

            "step_81": {# 2 TRIPOD LÁBAKAT LERAK, POZICIOK IDLE FEFEKVESHEZ BEALLITVA
                        #"RF": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa": 2060},
                        "RF": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 2060},
                        "RM": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa":  940},
                        #"LF": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa":  940},
                        "LF": {"pos_femur": 1737, "pos_tibia": 1747, "pos_coxa":  940},
                        "LM": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 2060}
                      },
                      
            "step_82": {# 1 TRIPOD LÁBAKAT EMEL, TRIPOD 2 POZICIOKAT TART IDLE LEFEKVESHEZ
                        #"RF": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa": 2060},
                        "RF": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 2060},
                        "RM": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1500}, # 1500
                        "RR": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa":  940},
                        #"LF": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa":  940}, # 1355
                        "LF": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa":  940}, # 1355
                        "LM": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 1500},
                        "LR": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 2060}  # 1644
                      },
                      
            "step_83": {# 1 TRIPOD LÁBAKAT LERAK, TRIPOD 2 POZICIOKAT TART IDLE LEFEKVESHEZ
                        #"RF": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa": 2060},
                        "RF": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 2060},
                        "RM": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa":  940},
                        #"LF": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa":  940},
                        "LF": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa":  940},
                        "LM": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 2060}
                      },
                      
            "step_84": {# IDLE POZICIO 
                        #"RF": {"pos_femur": 2450, "pos_tibia": 1800, "pos_coxa": 2060},
                        "RF": {"pos_femur":  550, "pos_tibia": 1200, "pos_coxa": 2060},
                        "RM": {"pos_femur": 2450, "pos_tibia": 1800, "pos_coxa": 1500},
                        "RR": {"pos_femur": 2450, "pos_tibia": 1800, "pos_coxa":  940},
                        #"LF": {"pos_femur":  550, "pos_tibia": 1150, "pos_coxa":  940},
                        "LF": {"pos_femur":  2450, "pos_tibia": 1850, "pos_coxa":  940},
                        "LM": {"pos_femur":  550, "pos_tibia": 1150, "pos_coxa": 1500},
                        "LR": {"pos_femur":  550, "pos_tibia": 1150, "pos_coxa": 2060}
                      }
             
                }
            
ret_to_rdy = {                      
            "step_1": {# 1 TRIPOD LÁBAKAT EMEL, CSÍPŐKET VÉGLEGES POZICIÓBA HOZ
                        #"RF": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 2060},
                        "RF": {"pos_femur": 1253, "pos_tibia": 1253, "pos_coxa": 2060},
                        "RM": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa":  940},
                        #"LF": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1355},
                        "LF": {"pos_femur":  2400, "pos_tibia": 2000, "pos_coxa": 1355},
                        "LM": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1500},
                        "LR": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1644}
                      },
                      
            "step_2": {# 1 TRIPOD LÁBAKAT LERAK
                        #"RF": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 2060},
                        "RF": {"pos_femur": 1253, "pos_tibia": 1253, "pos_coxa": 2060},
                        "RM": {"pos_femur": 1738, "pos_tibia": 1731, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa":  940},
                        #"LF": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1355},
                        "LF": {"pos_femur": 1729, "pos_tibia": 1792, "pos_coxa": 1355},
                        "LM": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1644}
                      },
                      
            "step_3": {# 2 TRIPOD LÁBAKAT EMEL, CSÍPŐKET VÉGLEGES POZICIÓBA HOZ
                        #"RF": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1644},
                        "RF": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1644},
                        "RM": {"pos_femur": 1738, "pos_tibia": 1731, "pos_coxa": 1500},
                        "RR": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1356},
                        #"LF": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1355},
                        "LF": {"pos_femur": 1729, "pos_tibia": 1792, "pos_coxa": 1355},
                        "LM": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1644}
                      },
                      
            "step_4": {# 2 TRIPOD LÁBAKAT LERAK
                        #"RF": {"pos_femur": 1729, "pos_tibia": 1792, "pos_coxa": 1644},
                        "RF": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1644},
                        "RM": {"pos_femur": 1738, "pos_tibia": 1731, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1729, "pos_tibia": 1792, "pos_coxa": 1356},
                        #"LF": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1355},
                        "LF": {"pos_femur": 1729, "pos_tibia": 1792, "pos_coxa": 1355},
                        "LM": {"pos_femur": 1262, "pos_tibia": 1269, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1644}
                      }          
                      
             }

reset_tripod_1 = {
            "step_1": {# 1 TRIPOD LÁBAKAT EMEL, CSÍPŐKET VÉGLEGES POZICIÓBA HOZ
                        "RM": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1500},
                        #"LF": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1355},
                        "LF": {"pos_femur":  2400, "pos_tibia": 2000, "pos_coxa": 1355},
                        "LR": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1644}
                      },
            "step_2": {# 1 TRIPOD LÁBAKAT LERAK
                        "RM": {"pos_femur": 1738, "pos_tibia": 1731, "pos_coxa": 1500},
                        #"LF": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1355},
                        "LF": {"pos_femur": 1729, "pos_tibia": 1792, "pos_coxa": 1355},
                        "LR": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1644}
                      }         
                 }

reset_tripod_2 = {
            "step_1": {# 2 TRIPOD LÁBAKAT EMEL, CSÍPŐKET VÉGLEGES POZICIÓBA HOZ
                        #"RF": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1644},
                        "RF": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1644},
                        "RR": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1356},
                        "LM": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1500},
                      },
            "step_2": {# 2 TRIPOD LÁBAKAT LERAK
                        #"RF": {"pos_femur": 1729, "pos_tibia": 1792, "pos_coxa": 1644},
                        "RF": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1644},
                        "RR": {"pos_femur": 1729, "pos_tibia": 1792, "pos_coxa": 1356},
                        "LM": {"pos_femur": 1262, "pos_tibia": 1269, "pos_coxa": 1500},                     
                      }
                 }

""" Definitions that used values from pos.py are saved here as an archive... """
"""
 def SetUpIdle(self):
        self.Update_Spdict(pos.pos_idle["step_1"], "all", "support", 500)

    def return_to_Idle(self):
        # READY pozícióból IDLE pozicíóba viszi a robotot
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
        # IDLE pozícióból READY pozicíóba viszi a robotot
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
        # IDLE pozícióból READY pozicíóba viszi a robotot
        self.Update_Spdict(pos.idle_to_rdy_v2["step_1"], "all", "swing", 500)
        self.Update_Spdict(pos.idle_to_rdy_v2["step_2"], "TripodB", "swing", 500) # TPA
        self.Update_Spdict(pos.idle_to_rdy_v2["step_3"], "TripodB", "swing", 250) # TPA
        self.Update_Spdict(pos.idle_to_rdy_v2["step_4"], "TripodA", "swing", 500) # TPB
        self.Update_Spdict(pos.idle_to_rdy_v2["step_5"], "TripodA", "swing", 250) # TPB

    def return_to_Ready(self):
        # Elvileg bármilyen pozícióbol READY pozícióba viszi a robotot
        self.Update_Spdict(pos.ret_to_rdy["step_1"], "TripodB", "swing", 500)
        self.Update_Spdict(pos.ret_to_rdy["step_2"], "TripodB", "swing", 500)
        self.Update_Spdict(pos.ret_to_rdy["step_3"], "TripodA", "swing", 500)
        self.Update_Spdict(pos.ret_to_rdy["step_4"], "TripodA", "swing", 500)

def go_to_Trans_I(self):
        self.Update_Spdict(pos.rdy_to_trns_1["step_1"])
        self.Update_Spdict(pos.rdy_to_trns_1["step_2"])
        self.Update_Spdict(pos.rdy_to_trns_1["step_3"])
        self.Update_Spdict(pos.rdy_to_trns_1["step_4"])
        self.Update_Spdict(pos.rdy_to_trns_1["step_5"])    

"""