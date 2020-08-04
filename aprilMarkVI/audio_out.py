import mp3play
from mutagen.mp3 import MP3
import sys
import time

f="audio.mp3"
audio = MP3(f)
length=audio.info.length
clip = mp3play.load(f)
clip.play()
time.sleep(length)
clip.stop()
