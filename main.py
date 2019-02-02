import blind_control as bc
from time import sleep

bc.open_completely()
sleep(50)
bc.close_completely()
sleep(50)
bc.tilt_percentage(50)
sleep(50)
bc.tilt_percentage(50)
