import time
import mp3play
from mutagen.mp3 import MP3
import sys
from gtts import gTTS

sorry="Sorry, I was not able to understand that."
print sorry
tts = gTTS(text=sorry, lang='en')
tts.save("sorry.mp3")
f="sorry.mp3"
audio = MP3(f)
length=audio.info.length
clip = mp3play.load(f)
clip.play()
time.sleep(length)
clip.stop()


