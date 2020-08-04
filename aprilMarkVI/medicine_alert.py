import socket
import time
import speech_recognition as sr
import sys
import time
from time import ctime
import pygame
import os
import alsaaudio
import sqlite3 as sql

def day_time():
    text=list(time.ctime().split(' '))
    #print text
    if text[2]!='':
	year=text[4]
	date=text[2]
	ti=list(text[3].split(':'))
	#print time[0],time[1],time[2]
	hh=ti[0]
	mm=ti[1]
	ss=ti[2]
	tim=""
	tim=hh+":"+mm
	#print text
	print tim
	#tim="The Time is "+tim
    else:
	year=text[5]
	date=text[3]
	ti=list(text[4].split(':'))
	#print time[0],time[1],time[2]
	hh=ti[0]
	mm=ti[1]
	ss=ti[2]
	tim=""
	tim=hh+":"+mm
	#print text
	print tim
	#tim="The Time is "+tim
    return tim


current_volume=0
m = alsaaudio.Mixer('PCM')
current_volume = m.getvolume()

while True:
    #print m.getvolume()
    con = sql.connect("medicine.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from details")

    rows = cur.fetchall();
    dosage=""
    med=""
    t=""
    meds=[]
    for r in rows:
	#print r
	t=r[2]
	#print t,day_time()
	if t==day_time():
	    me=[]
	    med=r[1]
	    dosage=r[3]
	    me.append(med)
	    me.append(dosage)
	    meds.append(me)
    for me in meds:
	print me
	current_volume = m.getvolume()
	m.setvolume(100)
	print "Its time to take "+me[1]+" of "+me[0]+"."
	os.system('/home/pi/April_mark_6_linux_version/./speak.sh "Its time to take '+me[1]+' of '+me[0]+'."')
	m.setvolume(int(current_volume[0]))
