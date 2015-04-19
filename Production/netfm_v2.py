import RPi.GPIO as GPIO # import knihovny pro ovladani GPIO pinu
import os               # import knihovny pro volani os 
from time import sleep

# cislo stanice
station_num = 0
 
# procedura volana pri preruseni - even detected
# predan parametr pin - tlacitko na kterem pinu bylo zmacknuto  
def my_event_callback_function(pin):
  global station_num
  print pin
  # pin 11 - stisknuto tlacitko pro zmenu cisla stanice
  if (pin == 11): 
    station_num = station_num + 1   
    # jen 8 stanic 
    if station_num == 8:
      station_num = 0
    print ('Prepocitavam! Nova stanice', station_num)
    # rozsviceni/zhasnuti LED s vahou 1
    if station_num in(1,3,5,7):
      GPIO.output(16, False)
    else:  
      GPIO.output(16, True)

    # rozsviceni/zhasnuti LED s vahou 2
    if station_num in(2,3,6,7):
      GPIO.output(18, False)
    else:  
      GPIO.output(18, True)

    # rozsviceni/zhasnuti LED s vahou 4
    if station_num in(4,5,6,7):
      GPIO.output(22, False)
    else:  
      GPIO.output(22, True)
      
  # pin 13 - stisknutu tlacitko pro spusteni prehravani
  if (pin == 13):
    print ('Prehravam stanici!', station_num)
    # zastavit prehravani aktualini stanice 
    retvalue = os.system("/home/pi/MyGPIO/killsox")
    sleep(1.5)
    # spusteni stanice podle promenne station_num
    if station_num == 1:
      retvalue = os.system("sox -v .9 -t mp3 http://pub8.radiotunes.com:80/radiotunes_country?d552732093489314cf927539 -t wav --input-buffer 80000 -r 22050 -c 1 - | sudo /home/pi/pifm/pifm - 98.0 &")
    elif station_num == 2:
      retvalue = os.system("sox -v .9 -t mp3 http://pub6.radiotunes.com:80/radiotunes_beatles?d552732093489314cf927539 -t wav --input-buffer 80000 -r 22050 -c 1 - | sudo /home/pi/pifm/pifm - 98.0 &")  
    elif station_num == 3:
      retvalue = os.system("sox -v .9 -t mp3 http://pub5.radiotunes.com:80/radiotunes_lovemusic?d552732093489314cf927539 -t wav --input-buffer 80000 -r 22050 -c 1 - | sudo /home/pi/pifm/pifm - 98.0 &")
    elif station_num == 4:
      retvalue = os.system("sox -v .9 -t mp3 http://pub7.radiotunes.com:80/radiotunes_relaxation?d552732093489314cf927539 -t wav --input-buffer 80000 -r 22050 -c 1 - | sudo /home/pi/pifm/pifm - 98.0 &")
    elif station_num == 5:
      retvalue = os.system("sox -v .9 -t mp3 http://pub4.radiotunes.com:80/radiotunes_cafedeparis?d552732093489314cf927539 -t wav --input-buffer 80000 -r 22050 -c 1 - | sudo /home/pi/pifm/pifm - 98.0 &")
    elif station_num == 6:
      retvalue = os.system("sox -v .9 -t mp3 http://pub2.radiotunes.com:80/radiotunes_smoothjazz247?d552732093489314cf927539 -t wav --input-buffer 80000 -r 22050 -c 1 - | sudo /home/pi/pifm/pifm - 98.0 &")
    elif station_num == 7:
      retvalue = os.system("sox -v .9 -t mp3 http://pub2.radiotunes.com:80/radiotunes_poprock?d552732093489314cf927539 -t wav --input-buffer 80000 -r 22050 -c 1 - | sudo /home/pi/pifm/pifm - 98.0 &")
  
  if (pin == 15):
    print ('Koncime!')
    # nastaveni stanice cislo 0
    station_num = 0
    # zhasnuti LED
    GPIO.output(16, True)
    GPIO.output(18, True)
    GPIO.output(22, True)  
    # vypnuti stanice
    retvalue = os.system("/home/pi/MyGPIO/killsox")
    sleep(1)
    # S timhle prikazem prestane vysilat, bude to sumet. 
    # Bez tohodle prikazu vysila ticho
    # GPIO.setup(7, GPIO.OUT) 
      
# nastaveni modu cislovani pinu na BOARD = fyzicka cisla pinu na desce
GPIO.setmode(GPIO.BOARD)

# nastaveni pinu pro LED
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

# zhasnuti led
# led jsou zapojeny tak, ze pri True je na Pinu napeti a led zhasne
GPIO.output(16, True)
GPIO.output(18, True)
GPIO.output(22, True)

# nastaveni pinu pro tlacitka. 
# Pull down urcuje zapojeni. Kde je odpor. Vypnute tlacitko = 0, zapnute = 1 
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# nastaveni tlacitek
# pri nabezne hrane se  vola procedura my_event_callback_function
# odpruzeni tlacitka 300 milisec.   
GPIO.add_event_detect(11, GPIO.RISING, callback=my_event_callback_function,  bouncetime=500 )
GPIO.add_event_detect(13, GPIO.RISING, callback=my_event_callback_function,  bouncetime=500 )
GPIO.add_event_detect(15, GPIO.RISING, callback=my_event_callback_function,  bouncetime=500 )
 
try:  
  while 1:
    pass;

except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  

GPIO.cleanup()           # clean up GPIO on normal exit  
