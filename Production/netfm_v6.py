import RPi.GPIO as GPIO # import knihovny pro ovladani GPIO pinu
import os               # import knihovny pro volani os 
from time import sleep

# cislo stanice
station_num = 0

# zapnutí prehravani mp3 
mp3_sw = 0
 
# procedura volana pri preruseni - even detected
# predan parametr pin - tlacitko na kterem pinu bylo zmacknuto  
def my_event_callback_function(pin):
  global station_num
  global mp3_sw
  print pin
  # vypnuti predchoziho prehravani
  print "vypinam predchozi prehravani" 
  retvalue = os.system("sudo /home/pi/pifm/pifmplay stop &")
  sleep(1)        
  retvalue = os.system("/home/pi/MyGPIO/killsox &")
  sleep(1)

  # pin 11 - stisknuto tlacitko pro start prehravani MP3
  if (pin == 11):
    print station_num
    print mp3_sw
    GPIO.output(16, False) # rozsvitim ledku 
    GPIO.output(18, True)
    GPIO.output(22, True)
'''     
    if (station_num > 0): 
      # vypnuti predchoziho prehravani
      print "vypinam predchozi prehravani" 
      retvalue = os.system("sudo /home/pi/pifm/pifmplay stop &")
      sleep(1)        
      retvalue = os.system("/home/pi/MyGPIO/killsox &")
      sleep(1)
''' 
    station_num = 0
    mp3_sw = 1
    print "poustim mp3"
    retvalue = os.system("sudo /home/pi/pifm/pifmplay /home/pi/MyMusic/ 98.0 &")
    return    
            
  # pin 13 - stisknuto tlacitko pro prehravani radia
  if (pin == 13):
    station_num = station_num + 1
    mp3_sw = 0   
    # jen 4 stanice 
    if station_num == 5:
      station_num = 1
    print ('Prepocitavam! Nova stanice', station_num)
    # rozsivit ledku pro radio
    GPIO.output(18, False)

    if station_num = (2,4):
      GPIO.output(16, False)
    else:  
      GPIO.output(16, True)
      
    # rozsviceni/zhasnuti LED s vahou 4
    if station_num in(3,4):
      GPIO.output(22, False)
    else:  
      GPIO.output(22, True)
      

    
'''    
    
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
      
    if (station_num == 1):
      print "jednicku po vypnuti"
      retvalue = os.system("sudo /home/pi/pifm/pifmplay /home/pi/MyMusic/ 98.0 &")      
    elif station_num == 2:
      retvalue = os.system("sox -v .9 -t mp3 http://pub8.radiotunes.com:80/radiotunes_country?d552732093489314cf927539 -t wav --input-buffer 80000 -r 22050 -c 1 - | sudo /home/pi/pifm/pifm - 98.0 &") 
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
'''      
      
  
  if (pin == 15):   # chci vypnout
    # zastavit prehravani aktualni stanice 
    print ('Koncime!')
    # nastaveni stanice cislo 0
    station_num = 0
    mp3_sw = 0      
    # zhasnuti LED
    GPIO.output(16, True)
    GPIO.output(18, True)
    GPIO.output(22, True)  

'''
    # vypnuti stanice
    retvalue = os.system("sudo /home/pi/pifm/pifmplay stop &")
    sleep(1)        
    retvalue = os.system("/home/pi/MyGPIO/killsox &")
    sleep(1)
'''    
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

''' 
pipe_name = '/home/pi/MyGPIO/mypipe'
try:  
  while 1:
    pipein = open(pipe_name, 'r')
    line = pipein.readline()
    print "A"+line+"B"
    if (line.find("0")>=0):
      print "Nula"
      retvalue = os.system("sox -v .9 -t mp3 http://pub4.radiotunes.com:80/radiotunes_cafedeparis?d552732093489314cf927539 -t wav --input-buffer 80000 -r 22050 -c 1 - | sudo /home/pi/pifm/pifm - 98.0 &")      
    pass;
'''

except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  

GPIO.cleanup()           # clean up GPIO on normal exit  
