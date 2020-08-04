import time
import mp3play
from mutagen.mp3 import MP3
import sys
from gtts import gTTS

thanq="It's my pleasure to be of assistance"
print thanq
tts = gTTS(text=thanq, lang='en')
tts.save("thanq.mp3")
f="thanq.mp3"
audio = MP3(f)
length=audio.info.length
clip = mp3play.load(f)
clip.play()
time.sleep(length)
clip.stop()


