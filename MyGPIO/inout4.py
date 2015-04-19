import RPi.GPIO as GPIO
import os
from time import sleep

def my_event_callback_function(pin):
    print('Callback function called!')
    print pin

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT) 
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(11, GPIO.RISING)
GPIO.add_event_callback(11, my_event_callback_function)

while 1:
  sleep(1)

GPIO.cleanup()           # clean up GPIO on normal exit  