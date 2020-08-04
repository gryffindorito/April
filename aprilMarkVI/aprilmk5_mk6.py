import socket
import time
import speech_recognition as sr
import sys
import time
from time import ctime
import pygame
import os
import alsaaudio
import random
from subprocess import check_output

import dtd

current_volume=0

m = alsaaudio.Mixer('PCM')
current_volume = m.getvolume()
pygame.mixer.init()

host='192.168.1.50'
port=1234

mic_name="Microphone (Realtek High Defini, MME (2 in, 0 out)"
sample_rate = 48000
chunk_size = 2048

r = sr.Recognizer()
 
mic_list = sr.Microphone.list_microphone_names()

device_id = 0
for i, microphone_name in enumerate(mic_list):
    if microphone_name == mic_name:
        device_id = i
        
tst=0
while True:
    with sr.Microphone(sample_rate = sample_rate, 
                            chunk_size = chunk_size) as source:

        r.dynamic_energy_threshold = False
        r.adjust_for_ambient_noise(source,1)
	if tst==0:
	    os.system('/home/pi/April_mark_6_linux_version/./speak.sh "I am Online"')
	    tst+=1
        print "Say Something"
        
        audio = r.listen(source)
             
        try:
            text = r.recognize_google(audio)
            print "you said: " + text
	    text=text.lower()
            inp=list(text.split(' '))
            if inp[0]=="April" or inp[0]=="april":
                if len(inp)==1:
		    print "Listening..."
		    """pygame.mixer.music.load("yes.mp3")
		    pygame.mixer.music.set_volume(1.0)
		    pygame.mixer.music.play()"""
		    os.system('/home/pi/April_mark_6_linux_version/./speak.sh "Yes ?"')
		    #while pygame.mixer.music.get_busy() == True:
		    #	pass
		    r.adjust_for_ambient_noise(source,1)
		    audio=r.listen(source)
		    text = r.recognize_google(audio)
		    print "you said: " + text
                else:
                    text=" ".join(inp[1:])
                   
                text=text.lower()
                text.strip(" ")
                i=text.split(' ')
		ala_com=""
		al_time=""
		sear=" ".join(i[:2])
                sear.strip(" ")
                sear2=" ".join(i[:3])
                sear2.strip(" ")
                ala=" ".join(i[:3])
                ala.strip(" ")
                vol_con=" ".join(i[:4])
                vol_con.strip(" ")
                vol_con2=" ".join(i[:3])
                vol_con2.strip(" ")
		
		
                if True:
		    if text=="light off":
			s=socket.socket()
			s.connect((host,port))
			string="0110"
			print "light off"
			s.send(string)
			s.close()
		    elif text=="light on":
			s=socket.socket()
			s.connect((host,port))
			string="0111"
			print "light on"
			s.send(string)
			s.close()
			    
		    elif text=="what's the date":
			dtd.day_date()
		    elif text=="what day is it today":
			dtd.day_day()
		    elif text=="what's the time":
			dtd.day_time()
		    elif text=="what time is it":
			dtd.day_time()
			
		    elif text=="what is your ip address":
			x=check_output(['hostname', '-I'])
			ip=x.split()
			ipaddr=ip[0]
			print ipaddr 
			os.system('/home/pi/April_mark_6_linux_version/./speak.sh "'+ipaddr +'"')
			
		    elif text=="set an alarm":
			f=open("command_alarm.txt",'w')
			f.write("")
			f.close()
			os.system("lxterminal -e python /home/pi/April_mark_6_linux_version/alarm.py")

		    elif ala=="wake me up":
			te=text.split(" ")
			time_alarm=" ".join(te[4:])
			time_alarm=time_alarm.strip(" ")
			f=open("command_alarm.txt",'w')
			f.write(time_alarm)
			f.close()
			os.system("lxterminal -e python /home/pi/April_mark_6_linux_version/alarm.py")
		    
		    elif i[0]=="remind":
			f=open("command_reminder.txt",'w')
			f.write(text)
			f.close()
			os.system("lxterminal -e python /home/pi/April_mark_6_linux_version/reminder.py")
			    
		    elif text=="mute":
			current_volume = m.getvolume()
			m.setvolume(0)
			print m.getvolume()
		    elif text=="unmute":
			cv=current_volume.split('L')
			m.setvolume(int(cv[0]))
			print m.getvolume()
		    elif text=="current volume":
			cv = m.getvolume()
			vol="Volume is at "+str(int(cv[0]))
			os.system('/home/pi/April_mark_6_linux_version/./speak.sh "'+vol+'"')
			print m.getvolume()
		    elif text=="volume":
			cv = m.getvolume()
			vol="Volume is at "+str(int(cv[0]))
			os.system('/home/pi/April_mark_6_linux_version/./speak.sh "'+vol+'"')
			print m.getvolume()
		    elif "set volume 200" in text:
			m.setvolume(100)
			print m.getvolume()
		    elif "set volume to" in text:
			vol=int((text.split(" "))[-1])
			m.setvolume(vol)
			print m.getvolume()
		    elif "increase volume by" in text:
			current_volume = m.getvolume()
			v=text.split(" ")
			vol=int(v[-1])
			if int(current_volume[0])+vol <=100:
			    m.setvolume(int(current_volume[0])+vol)
			else:
			    m.setvolume(100)
			print m.getvolume()
		    elif "decrease volume by" in text:
			current_volume = m.getvolume()
			v=text.split(" ")
			vol=int(v[-1])
			if int(current_volume[0])+vol >=0:
			    m.setvolume(int(current_volume[0])+vol)
			else:
			    m.setvolume(0)
			print m.getvolume()
		    
		    elif text=="tell me about yourself":
			abt_me="I am an assistant, currently being developed by Mr Arya. I can currently tell the date, day and time. I can also set alarms and reminders. My Birthday is in April that's hwy I was named April. Hope you and I can get familiar soon."
			print abt_me
			os.system('/home/pi/April_mark_6_linux_version/./speak.sh "'+abt_me+'"')
			    
		    else:
			print "Command not found"
			
	    elif text=="hello april":
                x=random.randint(1,3)
                if x==1:
		    os.system('/home/pi/April_mark_6_linux_version/./speak.sh "hello sir"')
                elif x==2:
		    os.system('/home/pi/April_mark_6_linux_version/./speak.sh "yes sir"')
                elif x==3:
		    os.system('/home/pi/April_mark_6_linux_version/./speak.sh "how are you sir"')

            elif text=="how are you april":
                x=random.randint(1,3)
                if x==1:
		    os.system('/home/pi/April_mark_6_linux_version/./speak.sh "I am fine sir"')
                elif x==2:
		    os.system('/home/pi/April_mark_6_linux_version/./speak.sh "I am good sir"')
                elif x==3:
		    os.system('/home/pi/April_mark_6_linux_version/./speak.sh "I am a machine, what do you expect "')
		    
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
         
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
