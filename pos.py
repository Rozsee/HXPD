<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 21:04:10 2018

@author: Rozsee
"""
pos_idle = {"step_1": {
                        "RF": {"pos_femur": 2450, "pos_tibia": 1800, "pos_coxa": 2060}, # pos_coxa was 2060
                        "RM": {"pos_femur": 2450, "pos_tibia": 1800, "pos_coxa": 1500},
                        "RR": {"pos_femur": 2450, "pos_tibia": 1800, "pos_coxa":  940},
                        "LF": {"pos_femur":  550, "pos_tibia": 1150, "pos_coxa":  940},
                        "LM": {"pos_femur":  550, "pos_tibia": 1150, "pos_coxa": 1500},
                        "LR": {"pos_femur":  550, "pos_tibia": 1150, "pos_coxa": 2060}
                      }
            }

idle_to_rdy = {
            "step_1": {# FELÁLL
                        "RF": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa": 2060},
                        "RM": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa":  940},
                        "LF": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa":  940},
                        "LM": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 2060}
                      },
            "step_2": {# 1 TRIPOD LÁBAKAT EMEL
                        "RF": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa": 2060},
                        "RM": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa":  940},
                        "LF": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa":  940},
                        "LM": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 1500},
                        "LR": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 2060}
                      },
            "step_3": {# 1 TRIPOD LÁBAKAT LERAK
                        "RF": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa": 2060},
                        "RM": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa":  940},
                        "LF": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa":  940},
                        "LM": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 2060}
                      },
            "step_4": {# 2 TRIPOD LÁBAKAT EMEL
                        "RF": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 2060},
                        "RM": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1500},
                        "RR": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa":  940},
                        "LF": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa":  940},
                        "LM": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 2060}
                      },
            "step_5": {# 2 TRIPOD LÁBAKAT LERAK
                        "RF": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 2060},
                        "RM": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa":  940},
                        "LF": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa":  940},
                        "LM": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 2060}
                      },
            "step_6": {# 1 TRIPOD LÁBAKAT EMEL, CSÍPŐKET VÉGLEGES POZICIÓBA HOZ
                        "RF": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 2060},
                        "RM": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa":  940},
                        "LF": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1355},
                        "LM": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1500},
                        "LR": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1644}
                      },
            "step_7": {# 1 TRIPOD LÁBAKAT LERAK
                        "RF": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 2060},
                        "RM": {"pos_femur": 1738, "pos_tibia": 1731, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa":  940},
                        "LF": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1355},
                        "LM": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1644}
                      },
            "step_8": {# 2 TRIPOD LÁBAKAT EMEL, CSÍPŐKET VÉGLEGES POZICIÓBA HOZ
                        "RF": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1644},
                        "RM": {"pos_femur": 1738, "pos_tibia": 1731, "pos_coxa": 1500},
                        "RR": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1356},
                        "LF": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1355},
                        "LM": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1644}
                      },
            "step_9": {# 2 TRIPOD LÁBAKAT LERAK
                        "RF": {"pos_femur": 1729, "pos_tibia": 1792, "pos_coxa": 1644},
                        "RM": {"pos_femur": 1738, "pos_tibia": 1731, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1729, "pos_tibia": 1792, "pos_coxa": 1356},
                        "LF": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1355},
                        "LM": {"pos_femur": 1262, "pos_tibia": 1269, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1644}
                      }
              }

rdy_to_idle = {
            "step_1": {# FELÁLL
                        "RF": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa": 2060},
                        "RM": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa":  940},
                        "LF": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa":  940},
                        "LM": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 2060}
                      },
            
            "step_3": {# 1 TRIPOD LÁBAKAT LERAK
                        "RF": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa": 2060},
                        "RM": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa":  940},
                        "LF": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa":  940},
                        "LM": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 2060}
                      },
            
            "step_5": {# 2 TRIPOD LÁBAKAT LERAK
                        "RF": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 2060},
                        "RM": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa":  940},
                        "LF": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa":  940},
                        "LM": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 2060}
                      },
            "step_6": {# 1 TRIPOD LÁBAKAT EMEL, CSÍPŐKET VÉGLEGES POZICIÓBA HOZ
                        "RF": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 2060},
                        "RM": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa":  940},
                        "LF": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1355},
                        "LM": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1500},
                        "LR": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1644}
                      },
           
            "step_8": {# 2 TRIPOD LÁBAKAT EMEL, CSÍPŐKET VÉGLEGES POZICIÓBA HOZ
                        "RF": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 2060}, # 1644
                        "RM": {"pos_femur": 1738, "pos_tibia": 1731, "pos_coxa": 1500}, 
                        "RR": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa":  940}, # 1356
                        "LF": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1355}, 
                        "LM": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1500}, # 1500
                        "LR": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1644}   
                      },

            "step_81": {# 2 TRIPOD LÁBAKAT LERAK, POZICIOK IDLE FEFEKVESHEZ BEALLITVA
                        "RF": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa": 2060},
                        "RM": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa":  940},
                        "LF": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa":  940},
                        "LM": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 2060}
                      },
                      
            "step_82": {# 1 TRIPOD LÁBAKAT EMEL, TRIPOD 2 POZICIOKAT TART IDLE LEFEKVESHEZ
                        "RF": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa": 2060},
                        "RM": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1500}, # 1500
                        "RR": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa":  940},
                        "LF": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa":  940}, # 1355
                        "LM": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 1500},
                        "LR": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 2060}  # 1644
                      },
                      
            "step_83": {# 1 TRIPOD LÁBAKAT LERAK, TRIPOD 2 POZICIOKAT TART IDLE LEFEKVESHEZ
                        "RF": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa": 2060},
                        "RM": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa":  940},
                        "LF": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa":  940},
                        "LM": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 2060}
                      },
                      
            "step_84": {# IDLE POZICIO 
                        "RF": {"pos_femur": 2450, "pos_tibia": 1800, "pos_coxa": 2060},
                        "RM": {"pos_femur": 2450, "pos_tibia": 1800, "pos_coxa": 1500},
                        "RR": {"pos_femur": 2450, "pos_tibia": 1800, "pos_coxa":  940},
                        "LF": {"pos_femur":  550, "pos_tibia": 1150, "pos_coxa":  940},
                        "LM": {"pos_femur":  550, "pos_tibia": 1150, "pos_coxa": 1500},
                        "LR": {"pos_femur":  550, "pos_tibia": 1150, "pos_coxa": 2060}
                      }
             
                }
            
ret_to_rdy = {                      
            "step_1": {# 1 TRIPOD LÁBAKAT EMEL, CSÍPŐKET VÉGLEGES POZICIÓBA HOZ
                        "RF": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 2060},
                        "RM": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa":  940},
                        "LF": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1355},
                        "LM": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1500},
                        "LR": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1644}
                      },
                      
            "step_2": {# 1 TRIPOD LÁBAKAT LERAK
                        "RF": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 2060},
                        "RM": {"pos_femur": 1738, "pos_tibia": 1731, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa":  940},
                        "LF": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1355},
                        "LM": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1644}
                      },
                      
            "step_3": {# 2 TRIPOD LÁBAKAT EMEL, CSÍPŐKET VÉGLEGES POZICIÓBA HOZ
                        "RF": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1644},
                        "RM": {"pos_femur": 1738, "pos_tibia": 1731, "pos_coxa": 1500},
                        "RR": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1356},
                        "LF": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1355},
                        "LM": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1644}
                      },
                      
            "step_4": {# 2 TRIPOD LÁBAKAT LERAK
                        "RF": {"pos_femur": 1729, "pos_tibia": 1792, "pos_coxa": 1644},
                        "RM": {"pos_femur": 1738, "pos_tibia": 1731, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1729, "pos_tibia": 1792, "pos_coxa": 1356},
                        "LF": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1355},
                        "LM": {"pos_femur": 1262, "pos_tibia": 1269, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1644}
                      }          
                      
             }

reset_tripod_1 = {
            "step_1": {# 1 TRIPOD LÁBAKAT EMEL, CSÍPŐKET VÉGLEGES POZICIÓBA HOZ
                        "RM": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1500},
                        "LF": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1355},
                        "LR": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1644}
                      },
            "step_2": {# 1 TRIPOD LÁBAKAT LERAK
                        "RM": {"pos_femur": 1738, "pos_tibia": 1731, "pos_coxa": 1500},
                        "LF": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1355},
                        "LR": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1644}
                      }         
                 }

reset_tripod_2 = {
            "step_1": {# 2 TRIPOD LÁBAKAT EMEL, CSÍPŐKET VÉGLEGES POZICIÓBA HOZ
                        "RF": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1644},
                        "RR": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1356},
                        "LM": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1500},
                      },
            "step_2": {# 2 TRIPOD LÁBAKAT LERAK
                        "RF": {"pos_femur": 1729, "pos_tibia": 1792, "pos_coxa": 1644},
                        "RR": {"pos_femur": 1729, "pos_tibia": 1792, "pos_coxa": 1356},
                        "LM": {"pos_femur": 1262, "pos_tibia": 1269, "pos_coxa": 1500},                     
                      }
                 }
=======
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 21:04:10 2018

@author: Rozsee
"""
pos_idle = {"step_1": {
                        "RF": {"pos_femur": 2450, "pos_tibia": 1800, "pos_coxa": 2060},
                        "RM": {"pos_femur": 2450, "pos_tibia": 1800, "pos_coxa": 1500},
                        "RR": {"pos_femur": 2450, "pos_tibia": 1800, "pos_coxa":  940},
                        "LF": {"pos_femur":  550, "pos_tibia": 1150, "pos_coxa":  940},
                        "LM": {"pos_femur":  550, "pos_tibia": 1150, "pos_coxa": 1500},
                        "LR": {"pos_femur":  550, "pos_tibia": 1150, "pos_coxa": 2060}
                      }
		    }

idle_to_rdy = {
            "step_1": {# FELÁLL
                        "RF": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa": 2060},
                        "RM": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa":  940},
                        "LF": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa":  940},
                        "LM": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 2060}
                      },
            "step_2": {# 1 TRIPOD LÁBAKAT EMEL
                        "RF": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa": 2060},
                        "RM": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa":  940},
                        "LF": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa":  940},
                        "LM": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 1500},
                        "LR": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 2060}
                      },
            "step_3": {# 1 TRIPOD LÁBAKAT LERAK
                        "RF": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa": 2060},
                        "RM": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa":  940},
                        "LF": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa":  940},
                        "LM": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 2060}
                      },
            "step_4": {# 2 TRIPOD LÁBAKAT EMEL
                        "RF": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 2060},
                        "RM": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1500},
                        "RR": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa":  940},
                        "LF": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa":  940},
                        "LM": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 2060}
                      },
            "step_5": {# 2 TRIPOD LÁBAKAT LERAK
                        "RF": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 2060},
                        "RM": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa":  940},
                        "LF": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa":  940},
                        "LM": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 2060}
                      },
            "step_6": {# 1 TRIPOD LÁBAKAT EMEL, CSÍPŐKET VÉGLEGES POZICIÓBA HOZ
                        "RF": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 2060},
                        "RM": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa":  940},
						"LF": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1355},
                        "LM": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1500},
                        "LR": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1644}
                      },
            "step_7": {# 1 TRIPOD LÁBAKAT LERAK
                        "RF": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 2060},
                        "RM": {"pos_femur": 1738, "pos_tibia": 1731, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa":  940},
						"LF": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1355},
                        "LM": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1644}
                      },
            "step_8": {# 2 TRIPOD LÁBAKAT EMEL, CSÍPŐKET VÉGLEGES POZICIÓBA HOZ
						"RF": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1644},
                        "RM": {"pos_femur": 1738, "pos_tibia": 1731, "pos_coxa": 1500},
						"RR": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1356},
						"LF": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1355},
						"LM": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1644}
                      },
            "step_9": {# 2 TRIPOD LÁBAKAT LERAK
						"RF": {"pos_femur": 1729, "pos_tibia": 1792, "pos_coxa": 1644},
                        "RM": {"pos_femur": 1738, "pos_tibia": 1731, "pos_coxa": 1500},
						"RR": {"pos_femur": 1729, "pos_tibia": 1792, "pos_coxa": 1356},
						"LF": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1355},
						"LM": {"pos_femur": 1262, "pos_tibia": 1269, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1644}
                      }
              }

rdy_to_idle = {
			"step_1": {# 2 TRIPOD LÁBAKAT EMEL, CSÍPŐKET VÉGLEGES POZICIÓBA HOZ
						"RF": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1644},
                        "RM": {"pos_femur": 1738, "pos_tibia": 1731, "pos_coxa": 1500},
						"RR": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1356},
						"LF": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1355},
						"LM": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1644}
                      },
			"step_2": {# 1 TRIPOD LÁBAKAT LERAK
                        "RF": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 2060},
                        "RM": {"pos_femur": 1738, "pos_tibia": 1731, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa":  940},
						"LF": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1355},
                        "LM": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1644}
                     },	
			"step_3": {# 1 TRIPOD LÁBAKAT EMEL, CSÍPŐKET VÉGLEGES POZICIÓBA HOZ
                        "RF": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 2060},
                        "RM": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa":  940},
						"LF": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1355},
                        "LM": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1500},
                        "LR": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1644}
                     },
			"step_4": {# 2 TRIPOD LÁBAKAT LERAK
                        "RF": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 2060},
                        "RM": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa":  940},
                        "LF": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa":  940},
                        "LM": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 2060}
                     },
			"step_5": {# 2 TRIPOD LÁBAKAT EMEL
                        "RF": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 2060},
                        "RM": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1500},
                        "RR": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa":  940},
                        "LF": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa":  940},
                        "LM": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 2060}
                     },
			"step_6": {# 1 TRIPOD LÁBAKAT LERAK
                        "RF": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa": 2060},
                        "RM": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa":  940},
                        "LF": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa":  940},
                        "LM": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 2060}
                     },
			"step_7": {# 1 TRIPOD LÁBAKAT EMEL
                        "RF": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa": 2060},
                        "RM": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa":  940},
                        "LF": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa":  940},
                        "LM": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 1500},
                        "LR": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 2060}
                     },
			"step_8": {# FELÁLL
                        "RF": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa": 2060},
                        "RM": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1716, "pos_tibia": 1483, "pos_coxa":  940},
                        "LF": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa":  940},
                        "LM": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1284, "pos_tibia": 1517, "pos_coxa": 2060}
                     },
			    }
            
reset_tripod_1 = {
            "step_1": {# 1 TRIPOD LÁBAKAT EMEL, CSÍPŐKET VÉGLEGES POZICIÓBA HOZ
						"RM": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1500},
                        "LF": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1355},
                        "LR": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1644}
					  },
            "step_2": {# 1 TRIPOD LÁBAKAT LERAK
                        "RM": {"pos_femur": 1738, "pos_tibia": 1731, "pos_coxa": 1500},
						"LF": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1355},
                        "LR": {"pos_femur": 1271, "pos_tibia": 1208, "pos_coxa": 1644}
                      }         
                 }

reset_tripod_2 = {
            "step_1": {# 2 TRIPOD LÁBAKAT EMEL, CSÍPŐKET VÉGLEGES POZICIÓBA HOZ
						"RF": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1644},
                        "RR": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1356},
						"LM": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1500},
                      },
            "step_2": {# 2 TRIPOD LÁBAKAT LERAK
						"RF": {"pos_femur": 1729, "pos_tibia": 1792, "pos_coxa": 1644},
						"RR": {"pos_femur": 1729, "pos_tibia": 1792, "pos_coxa": 1356},
						"LM": {"pos_femur": 1262, "pos_tibia": 1269, "pos_coxa": 1500},						
                      }
                 }
"""
rdy_to_trns_1 = {
			"step_1": {# LF emel
    						"RF": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1800},
                        "RM": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1200},
                        "LF": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1200},
                        "LM": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1800}
                      },
			"step_2": {#LF lerak, RR emel
    						"RF": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1800},
                        "RM": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1500},
                        "RR": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1200},
                        "LF": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1880},
                        "LM": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1800}
                      },
			"step_3": {# RR lerak, RF emel
    						"RF": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1800},
                        "RM": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1880},
                        "LF": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1880},
                        "LM": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1800}
                      },
			"step_4": {#RF lerak, LR emel
    						"RF": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1120},
                        "RM": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1880},
                        "LF": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1880},
                        "LM": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1500},
                        "LR": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1800}
                      },
			"step_5": {#LR lerak
    						"RF": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1120},
                        "RM": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1880},
                        "LF": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1880},
                        "LM": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1120}
                      }
				  }
            
trns_1_to_rdy = {
			"step_4": {#RF lerak, LR emel
    						"RF": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1120},
                        "RM": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1880},
                        "LF": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1880},
                        "LM": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1500},
                        "LR": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1800}
                     },
			"step_3": {# RR lerak, RF emel
    						"RF": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1800},
                        "RM": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1880},
                        "LF": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1880},
                        "LM": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1800}
                     },
			"step_2": {#LF lerak, RR emel
    						"RF": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1880},
                        "RM": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1500},
                        "RR": {"pos_femur": 2400, "pos_tibia": 2000, "pos_coxa": 1200},
                        "LF": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1880},
                        "LM": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1800}
                     },
			"step_1": {# LF emel
    						"RF": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1800},
                        "RM": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1500},
                        "RR": {"pos_femur": 1747, "pos_tibia": 1747, "pos_coxa": 1200},
                        "LF": {"pos_femur":  600, "pos_tibia": 1000, "pos_coxa": 1200},
                        "LM": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1500},
                        "LR": {"pos_femur": 1263, "pos_tibia": 1253, "pos_coxa": 1800}
                     },
				}
"""
>>>>>>> 7d52a3a5c13e4c4f6a9002e5690495c93f9deec0
