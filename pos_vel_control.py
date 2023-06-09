from moteus_fdcan_adapter import Controller
from moteus_fdcan_adapter import MoteusReg
import time
import math
               

def setposvel(pos,vel):
    controller_1 = Controller(controller_ID = 1)
    response_data_c1=controller_1.get_data()
    pos_deg_c1 = response_data_c1[MoteusReg.MOTEUS_REG_POSITION]
    if (pos_deg_c1>pos):
        
        vel=vel*-1
        while(1):
            
            response_data_c1=controller_1.get_data()
            pos_deg_c1 = response_data_c1[MoteusReg.MOTEUS_REG_POSITION]
            print(pos_deg_c1)
            if (pos_deg_c1<=pos):
                break
            controller_1.set_velocity(velocity=vel)
    else: 
        
        while(1):
            
            response_data_c1=controller_1.get_data()
            pos_deg_c1 = response_data_c1[MoteusReg.MOTEUS_REG_POSITION]
            print(pos_deg_c1)
            if (pos_deg_c1>=pos):
                break
            if abs(pos_deg_c1-pos)<0.05:
                vel=0.5
            controller_1.set_velocity(velocity=vel)

    
    pass    



def main():
    controller_1 = Controller(controller_ID = 1)
    setposvel(0,0.5)  #0
    response_data_c1=controller_1.get_data()
    pos_deg_c1 = response_data_c1[MoteusReg.MOTEUS_REG_POSITION]
    print(pos_deg_c1)
    time.sleep(3)
    setposvel(0.5,0.5)  #180
    response_data_c1=controller_1.get_data()
    pos_deg_c1 = response_data_c1[MoteusReg.MOTEUS_REG_POSITION]
    print(pos_deg_c1)
    time.sleep(3)
    setposvel(-0.487,1.5) #-175
    response_data_c1=controller_1.get_data()
    pos_deg_c1 = response_data_c1[MoteusReg.MOTEUS_REG_POSITION]
    print(pos_deg_c1)
    time.sleep(0.5)

    setposvel(0.954,0.8)  #343
    while(1):
        response_data_c1=controller_1.get_data()
        pos_deg_c1 = response_data_c1[MoteusReg.MOTEUS_REG_POSITION]
        print(pos_deg_c1)

    

if __name__ == '__main__':
    main()