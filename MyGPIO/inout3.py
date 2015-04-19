import RPi.GPIO as GPIO
import os
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT) 
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while 1:
  print "Cekam na zmacknuti"
  GPIO.output(13, True)  
  GPIO.wait_for_edge(11, GPIO.RISING)  
  GPIO.output(13, False)
  # retvalue = os.system("sox -v .9 -t mp3 http://pub4.sky.fm:80/sky_cafedeparis?d552732093489314cf927539 -t wav --input-buffer 80000 -r 22050 -c 1 - | sudo /home/pi/pifm/pifm - 98.0")
  # print retvalue
  print "Zmacknuto"
  print "Cekam na pusteni"
  GPIO.wait_for_edge(11, GPIO.FALLING)  
  print "Pusteno"  

# GPIO.cleanup()           # clean up GPIO on normal exit  