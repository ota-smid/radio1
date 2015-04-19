#!/usr/bin/env python
import os               # import knihovny pro volani os 
print "Content-type: text/html\n\n"
print "<h1>Hello World</h1>"
os.system("sudo /home/pi/pifm/pifm /home/pi/pifm/sound.wav 98.0 &")
