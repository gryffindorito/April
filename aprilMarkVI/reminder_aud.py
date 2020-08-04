import speech_recognition as sr
import mp3play
from mutagen.mp3 import MP3
import sys
import time
from time import ctime
import time
import os
from gtts import gTTS
tts = gTTS(text="What do you want to be reminded ?", lang='en')
tts.save("reminder_aud.mp3")
f="reminder_aud.mp3"
audio = MP3(f)
length=audio.info.length
clip = mp3play.load(f)
clip.play()
time.sleep(length)
clip.stop()
