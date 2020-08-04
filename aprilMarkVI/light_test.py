import socket
import time
import speech_recognition as sr
import sys
import time
from time import ctime
import pygame
import os

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
        
while True:
    with sr.Microphone(sample_rate = sample_rate, 
                            chunk_size = chunk_size) as source:

        r.dynamic_energy_threshold = False
        r.adjust_for_ambient_noise(source,1)
        print "Say Something"
        
        audio = r.listen(source)
             
        try:
            text = r.recognize_google(audio)
            print "you said: " + text
            inp=list(text.split(' '))
            if inp[0]=="Light" or inp[0]=="light":
                if len(inp)==1:
					print "Listening..."
					pygame.mixer.music.load("yes.mp3")
					pygame.mixer.music.set_volume(1.0)
					pygame.mixer.music.play()
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
                if True:
					if text=="on":
						s=socket.socket()
						s.connect((host,port))
						string="0110"
						print "light on"
						s.send(string)
						s.close()
					elif text=="off":
						s=socket.socket()
						s.connect((host,port))
						string="0111"
						print "light off"
						s.send(string)
						s.close()
                """
                if text=="switch on light":
					s=socket.socket()
					s.connect((host,port))
					string="0110"
					print "light on"
					s.send(string)
					s.close()
				elif text=="switch off light":
					pass
				elif text=="switch off light":
					s=socket.socket()
					s.connect((host,port))
					string="0111"
					print "light off"
					s.send(string)
					s.close()
				else:
					pass
			else:
				pass"""
				
					
                        
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
         
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
