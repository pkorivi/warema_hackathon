import blind_control as bc
from time import sleep

bc.open_completely()
sleep(20)
bc.close_completely()
sleep(20)
bc.tilt_down(50)
sleep(50)
bc.tilt_up(50)
