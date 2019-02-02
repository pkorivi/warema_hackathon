import automationhat as ah
from time import sleep

def open_completely():
    open_percentage(100)

def open_percentage(value):
    ah.relay.one.on()
    sleep((value/100.0)*36.0)
    ah.relay.one.off()

def close_percentage(value):
    ah.relay.two.on()
    sleep((value/100.0)*36.0)
    ah.relay.two.off()

def close_completely():
    close_percentage(100)

def tilt_percentage(value):
    ah.relay.one.on()
    sleep((value/100)*0.8)
    ah.relay.one.off()
    
