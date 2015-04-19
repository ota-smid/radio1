#!/bin/bash

echo -e "Content-type: text/html\n\n"

echo "<h1>Hello World from SGI </h1>"

# sudo  ls > a.lst
# sudo /usr/lib/cgi-bin/radio/rstart


echo "
<form action="http://10.0.0.42/cgi-bin/radio/test.cgi" method="POST">
<input type="submit">
</form>"


