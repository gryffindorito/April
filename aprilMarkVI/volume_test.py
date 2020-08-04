import alsaaudio
m = alsaaudio.Mixer('PCM')
current_volume = m.getvolume() # Get the current Volume
print current_volume
m.setvolume(100) # Set the volume to 70%.
