import RPi.GPIO as GPIO
import os
from time import sleep

station_num = 0
 
def my_event_callback_function(pin):
  global station_num
  print('Callback function called!')
  print pin
  if (pin == 11): 
    station_num = station_num + 1    
    if station_num == 8:
      station_num = 0
    print ('Prepocitavam! Nova stanice', station_num)
           
  if (pin == 16):
    print ('Prehravam stanici!', station_num)
    retvalue = os.system("/home/pi/MyGPIO/killsox")
    sleep(1.5)
    if station_num == 1:
      retvalue = os.system("sox -v .9 -t mp3 http://pub4.sky.fm:80/sky_cafedeparis?d552732093489314cf927539 -t wav --input-buffer 80000 -r 22050 -c 1 - | sudo /home/pi/pifm/pifm - 98.0 &")
    elif station_num == 2:
      retvalue = os.system("sox -v .9 -t mp3 http://icecast5.play.cz:8000/cro1-32.mp3 -t wav --input-buffer 80000 -r 22050 -c 1 - | sudo /home/pi/pifm/pifm - 98.0 &")
    elif station_num == 3:
      retvalue = os.system("sox -v .9 -t mp3 http://pub4.sky.fm:80/sky_cafedeparis?d552732093489314cf927539 -t wav --input-buffer 80000 -r 22050 -c 1 - | sudo /home/pi/pifm/pifm - 98.0 &")
    elif station_num == 4:
      retvalue = os.system("sox -v .9 -t mp3 http://icecast5.play.cz:8000/cro1-32.mp3 -t wav --input-buffer 80000 -r 22050 -c 1 - | sudo /home/pi/pifm/pifm - 98.0 &")
    elif station_num == 5:
      retvalue = os.system("sox -v .9 -t mp3 http://pub4.sky.fm:80/sky_cafedeparis?d552732093489314cf927539 -t wav --input-buffer 80000 -r 22050 -c 1 - | sudo /home/pi/pifm/pifm - 98.0 &")
    elif station_num == 6:
      retvalue = os.system("sox -v .9 -t mp3 http://icecast5.play.cz:8000/cro1-32.mp3 -t wav --input-buffer 80000 -r 22050 -c 1 - | sudo /home/pi/pifm/pifm - 98.0 &")
    elif station_num == 7:
      retvalue = os.system("sox -v .9 -t mp3 http://pub4.sky.fm:80/sky_cafedeparis?d552732093489314cf927539 -t wav --input-buffer 80000 -r 22050 -c 1 - | sudo /home/pi/pifm/pifm - 98.0 &")
  
  if (pin == 18):
    print ('Koncime!')
    station_num = 0  
    retvalue = os.system("/home/pi/MyGPIO/killsox")
    sleep(1)
    
'''    
'''
   
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT) 
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(11, GPIO.RISING, callback=my_event_callback_function,  bouncetime=300 )
GPIO.add_event_detect(16, GPIO.RISING, callback=my_event_callback_function,  bouncetime=300 )
GPIO.add_event_detect(18, GPIO.RISING, callback=my_event_callback_function,  bouncetime=300 )
 
try:  
  while 1:
    pass;

except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  

GPIO.cleanup()           # clean up GPIO on normal exit  