from flask import Flask
from flask_ask import Ask, statement, convert_errors
import RPi.GPIO as GPIO
import logging

GPIO.setmode(GPIO.BCM)

app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.intent('blinds', mapping={})
def gpio_control(status, pin):
    print "got control here "

    #try:
    #    pinNum = int(pin)
    #except Exception as e:
    #    return statement('Pin number not valid.')

    #GPIO.setup(pinNum, GPIO.OUT)

    #if status in ['on', 'high']:    GPIO.output(pinNum, GPIO.HIGH)
    #if status in ['off', 'low']:    GPIO.output(pinNum, GPIO.LOW)

    return statement('blinds something')
