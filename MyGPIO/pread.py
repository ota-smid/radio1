import os
pipe_name = 'mypipe'

while True:
  pipein = open(pipe_name, 'r')
  line = pipein.readline()
  print line

