from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
import pygame
import sys
import time
from time import ctime
import os
from gtts import gTTS
global text

pygame.mixer.init()

text=""
f=0
fp=open("command_search.txt",'r')
for line in fp:
    if f==0:
        text=line
    f=f+1
fp.close
print text
driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
driver.get("https://www.wikipedia.org/")
elem = driver.find_element_by_name("search")
elem.clear()
elem.send_keys(text)
elem.send_keys(Keys.ENTER)
data=driver.find_element_by_xpath("//*[@id='mw-content-text']/div/p[1]").text
print data.encode("utf-8")
#assert "No results found." not in driver.page_source
driver.close()
tts = gTTS(text=data, lang='en')
tts.save("result.mp3")
pygame.mixer.music.load("result.mp3")
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy() == True:
    pass
