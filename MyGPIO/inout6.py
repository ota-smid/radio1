import RPi.GPIO as GPIO
import os
from time import sleep

station_num = 0
 
def my_event_callback_function(pin):
  global station_num
  print pin
  if (pin == 11): 
    station_num = station_num + 1    
    if station_num == 8:
      station_num = 0
    print ('Prepocitavam! Nova stanice', station_num)
    if station_num in(1,3,5,7):
      GPIO.output(16, False)
    else:  
      GPIO.output(16, True)

    if station_num in(2,3,6,7):
      GPIO.output(18, False)
    else:  
      GPIO.output(18, True)

    if station_num in(4,5,6,7):
      GPIO.output(22, False)
    else:  
      GPIO.output(22, True)
      
  if (pin == 13):
    print ('Prehravam stanici!', station_num)
    retvalue = os.system("/home/pi/MyGPIO/killsox")
    sleep(1.5)
    if station_num == 1:
      retvalue = os.system("sox -v .9 -t mp3 http://pub8.sky.fm:80/sky_country?d552732093489314cf927539 -t wav --input-buffer 80000 -r 22050 -c 1 - | sudo /home/pi/pifm/pifm - 98.0 &")
    elif station_num == 2:
      retvalue = os.system("sox -v .9 -t mp3 http://pub6.sky.fm:80/sky_beatles?d552732093489314cf927539 -t wav --input-buffer 80000 -r 22050 -c 1 - | sudo /home/pi/pifm/pifm - 98.0 &")  
    elif station_num == 3:
      retvalue = os.system("sox -v .9 -t mp3 http://pub5.sky.fm:80/sky_lovemusic?d552732093489314cf927539 -t wav --input-buffer 80000 -r 22050 -c 1 - | sudo /home/pi/pifm/pifm - 98.0 &")
    elif station_num == 4:
      retvalue = os.system("sox -v .9 -t mp3 http://pub7.sky.fm:80/sky_relaxation?d552732093489314cf927539 -t wav --input-buffer 80000 -r 22050 -c 1 - | sudo /home/pi/pifm/pifm - 98.0 &")
    elif station_num == 5:
      retvalue = os.system("sox -v .9 -t mp3 http://pub4.sky.fm:80/sky_cafedeparis?d552732093489314cf927539 -t wav --input-buffer 80000 -r 22050 -c 1 - | sudo /home/pi/pifm/pifm - 98.0 &")
    elif station_num == 6:
      retvalue = os.system("sox -v .9 -t mp3 http://pub2.sky.fm:80/sky_smoothjazz247?d552732093489314cf927539 -t wav --input-buffer 80000 -r 22050 -c 1 - | sudo /home/pi/pifm/pifm - 98.0 &")
    elif station_num == 7:
      retvalue = os.system("sox -v .9 -t mp3 http://pub2.sky.fm:80/sky_poprock?d552732093489314cf927539 -t wav --input-buffer 80000 -r 22050 -c 1 - | sudo /home/pi/pifm/pifm - 98.0 &")
  
  if (pin == 15):
    print ('Koncime!')
    station_num = 0
    GPIO.output(16, True)
    GPIO.output(18, True)
    GPIO.output(22, True)  
    retvalue = os.system("/home/pi/MyGPIO/killsox")
    sleep(1)
    # S timhle prikazem prestane vysilat, bude to sumet. 
    # Bez tohodle prikazu vysila ticho
    # GPIO.setup(7, GPIO.OUT) 
      
GPIO.setmode(GPIO.BOARD)

GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

GPIO.output(16, True)
GPIO.output(18, True)
GPIO.output(22, True)

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(11, GPIO.RISING, callback=my_event_callback_function,  bouncetime=300 )
GPIO.add_event_detect(13, GPIO.RISING, callback=my_event_callback_function,  bouncetime=300 )
GPIO.add_event_detect(15, GPIO.RISING, callback=my_event_callback_function,  bouncetime=300 )
 
try:  
  while 1:
    pass;

except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  

GPIO.cleanup()           # clean up GPIO on normal exit  