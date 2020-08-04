import time
import mp3play
from mutagen.mp3 import MP3
import sys
from gtts import gTTS

abt_me="I am an assistant, currently being developed by Mr Arya. I can currently tell the date, day and time. I can also set alarms and reminders. My Birthday is in April that's hwy I was named April. Hope you and I can get familiar soon."
print abt_me
tts = gTTS(text=abt_me, lang='en')
tts.save("about_me.mp3")
f="about_me.mp3"
audio = MP3(f)
length=audio.info.length
clip = mp3play.load(f)
clip.play()
time.sleep(length)
clip.stop()


