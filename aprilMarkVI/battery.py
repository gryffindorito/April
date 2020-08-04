import time
import mp3play
from mutagen.mp3 import MP3
import sys
from gtts import gTTS

import psutil

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = int(battery.percent)
if plugged==False: plugged="Dropping"
else: plugged="Charging"
battery=""
if percent==100 and plugged==False:
    battery="The power level is "+str(percent)+"% and "+plugged
if percent==100 and plugged==True:
    battery="The power level is "+str(percent)+"% and Stable"
else:
    battery="The power level is "+str(percent)+"% and "+plugged
print battery
tts = gTTS(text=battery, lang='en')
tts.save("battery.mp3")
f="battery.mp3"
audio = MP3(f)
length=audio.info.length
clip = mp3play.load(f)
clip.play()
time.sleep(length)
clip.stop()
