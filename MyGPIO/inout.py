import RPi.GPIO as GPIO
import os
import time

cur_station_num = 0
req_station_num = 0
time_stamp = time.time()
 
def my_event_callback_function(pin):
  global req_station_num
  global time_stamp
  time_stamp = time.time()
  req_station_num = req_station_num + 1
  if req_station_num == 8:
    req_station_num = 0 
  print('Callback function called!')
  print pin
  print req_station_num

def setup_station(loc_st):
  global req_station_num
  req_station_num = req_station_num + 1
  print('Ladim!', loc_st) 
  retvalue = os.system("/home/pi/MyGPIO/killsox &")
  ''' Multi comment  
  time.sleep(1)  
  if loc_st == 1:
    pass
    # retvalue = os.system("sox -v .9 -t mp3 http://pub4.sky.fm:80/sky_cafedeparis?d552732093489314cf927539 -t wav --input-buffer 80000 -r 22050 -c 1 - | sudo /home/pi/pifm/pifm - 98.0 &")  
  elif loc_st == 2:
    print('1')
    pass 
    # retvalue = os.system("sox -v .9 -t mp3 http://icecast5.play.cz:8000/cro1-32.mp3 -t wav --input-buffer 80000 -r 22050 -c 1 - | sudo /home/pi/pifm/pifm - 98.0 &")
    print('2') 
  else:
    pass 
    # retvalue = os.system("/home/pi/MyGPIO/killsox &")   
  print('Nalazeno')   
'''   
''' Multi comment  
'''

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT) 
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(11, GPIO.RISING, callback=my_event_callback_function,  bouncetime=200 )
 # callback=lambda x: buttonPressed(50), bouncetime=2000)
# GPIO.add_event_callback(11, my_event_callback_function)

try:  
  while 1:
    pass
    # time.sleep(1)
    print req_station_num
    if (req_station_num == 2):
      print('Stanice 2')
      setup_station(req_station_num)
    else:
      print('Cekam na preruseni')
      # time.sleep(1)
        
    ''' Multi comment 
    if (cur_station_num <> req_station_num) and ((time.time() - time_stamp) >= 1):
      print('Preladujeme!')
      setup_station(req_station_num)
      print('Po ladeni')
      time_stamp = time.time()
      cur_station_num = req_station_num
    else: 
      print('Cekam na preruseni')
      time.sleep(1)
      ''' 
      

except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  

GPIO.cleanup()           # clean up GPIO on normal exit  