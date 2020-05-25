#!/bin/bash
#

sudo apt-get -yy update
sudo apt-get -yy install python3-requests

wget https://raw.githubusercontent.com/rmoesbergen/teletekst/master/teletekst.py -O /home/pi/teletekst.py
chmod +x /home/pi/teletekst.py

# Install cron job a 1 minute past midnight
echo "1 0 * * * pi /home/pi/teletekst.py '/home/pi/teletekst-%m.csv'" | sudo tee /etc/cron.d/teletekst
