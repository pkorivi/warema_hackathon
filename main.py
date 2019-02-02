import blind_control as bc
from time import sleep

maxim_light=2.2
auto_array=[]

sensor_nise_filter=0
state = False
prev_state = False

down_state = False
prev_down_state = False

while(1):
    
    light_valu=bc.read_light()
    print(light_valu)
    
    if(light_valu>3):
       sensor_nise_filter=1
    
    if(sensor_nise_filter==0):
        if(light_valu>maxim_light):
            state=True
        else:
            state = False
            
    if(prev_state!=state and state == True):        
        bc.tilt_up(100)
        auto_array.append(light_valu)
        print(auto_array)
        
    prev_state = state  
    sensor_nise_filter=0
    switch = bc.read_switch()
    if(switch>3):
        down_state = True
    else:
        down_state = False

    if(down_state != prev_down_state and down_state == True):
            bc.tilt_down(100)

    prev_down_state = down_state
                        
    sleep(0.5)
    

