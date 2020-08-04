import sys
import time
import os
import pygame

pygame.mixer.init()

import datetime
text=""
print "on"
try:
    fp=open("command_reminder.txt",'r')
    for line in fp:
        text=line
    fp.close
except:
    pass     

text=text.lower()
noise_list=["at","to","april","in"]
text=text.strip().split(' ')
if ("remind" in text) and ("me" in text) and ("to" in text) :
    noise_free_words = [word for word in text if word not in noise_list] 
    noise_free_text = " ".join(noise_free_words)

print noise_free_text
noise_free_text=noise_free_text.split(' ')
command = noise_free_text[0]
wo = " ".join(noise_free_words[2:-2])
w=wo.split(' ')
work=""
for wor in w:
    if wor=="my":
        work=work+" your "
    else:
        work=work+" "+wor
time1 = noise_free_text[-2]+" "+noise_free_text[-1]

print command,"     ",work,"      ",time1

time1=time1.split(' ')
global hr
global mins
if "o" in time1[1]:
    hr= time1[0]
    mins=time1[2]
else:
    t=time1[0]
    t=t.split(":")
    hr=t[0]
    try:
        mins=t[1]
    except:
        mins="00"
        
if time1[1]=="a.m." or time1[1]=="a.m" :
    if hr=="12":
        hr=str(int(hr)-12)
elif time1[1]=="p.m." or time1[1]=="p.m":
    hr=str(int(hr)+12)
print hr,mins
while True:
    rn = str(datetime.datetime.now().time())
    rn=rn.split(":")
    hr1=rn[0]
    mins1=rn[1]
    print hr,mins,"     ",hr1,mins1
    if int(hr)==int(hr1) and int(mins)==int(mins1):
        print "alarm"
        break
        
for i in range(0,1):
pygame.mixer.music.load("alarm_tone.mp3")
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy() == True:
    pass

os.system('/home/pi/April_mark_6_linux_version/./speak.sh " Sir you have a reminder to '+work+'"')

