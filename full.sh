
#!/bin/bash
TOD=$(date +%Y-%m-%d_%H%M)
YR=$(date +%Y)
MON=$(date +%m)
DAY=$(date +%d)

cd /home/pi/jdconey.github.io/
#git clone https://github.com/jdconey/jdconey.github.io.git
git pull


. /home/pi/winter_code/cairngorm.sh
. /home/pi/winter_code/glencoe.sh
. /home/pi/winter_code/nevis_range.sh
python3 /home/pi/winter_code/bennevis.py

git add *
git commit -m $TOD
git push