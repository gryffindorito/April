import os
import time
import sys

def day_date():
	text=list(time.ctime().split(' '))
	day_s=['Mon','Tue','Wed','Thur','Fri','Sat','Sun'];
	day=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
	month_s=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
	month=['January','February','March','April','May','June','July','August','September','Octber','November','December']
	if text[2]!='':
		year=text[4]
		date=text[2]
		ti=list(text[3].split(':'))
		#print time[0],time[1],time[2]
		hh=ti[0]
		mm=ti[1]
		ss=ti[2]
		#if hh >12 and hh!=24:
		#    hh=int(hh)-12
		#    print hh,":",mm," pm"
		#elif hh==24:
		#        print "00:",mm," am"
		#else:
		#    print hh,":",mm," am"
		#print text
		mon=month[month_s.index(text[1])]
		print date, mon,year
		t=date+" "+mon+" "+year
	else:
		year=text[5]
		date=text[3]
		ti=list(text[4].split(':'))
		#print time[0],time[1],time[2]
		hh=ti[0]
		mm=ti[1]
		ss=ti[2]
		#if hh >12 and hh!=24:
		#    hh=int(hh)-12
		#    print hh,":",mm," pm"
		#elif hh==24:
		#        print "00:",mm," am"
		#else:
		#    print hh,":",mm," am"
		#print text
		mon=month[month_s.index(text[1])]
		print date, mon,year
		t=str(date)+" "+str(mon)+" "+str(year)
	os.system('/home/pi/April_mark_6_linux_version/./speak.sh "'+t+'"')
	
def day_time():
	text=list(time.ctime().split(' '))
	day_s=['Mon','Tue','Wed','Thur','Fri','Sat','Sun'];
	day=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
	month_s=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
	month=['January','February','March','April','May','June','July','August','September','Octber','November','December']
	if text[2]!='':
		year=text[4]
		date=text[2]
		ti=list(text[3].split(':'))
		#print time[0],time[1],time[2]
		hh=int(ti[0])
		mm=int(ti[1])
		ss=ti[2]
		tim=""
		if hh >12 and hh!=24:
			hh=int(hh)-12
			hh=str(hh)
			tim=str(hh)+":"+str(mm)+" pm"
		elif hh==24:
				tim="00:"+mm+" am"
		else:
			tim=str(hh)+":"+str(mm)+" am"
		#print text
		print tim
		tim="The Time is "+tim
	else:
		year=text[5]
		date=text[3]
		ti=list(text[4].split(':'))
		#print time[0],time[1],time[2]
		hh=int(ti[0])
		mm=(ti[1])
		ss=ti[2]
		tim=""
		if hh >12 and hh!=24:
			hh=int(hh)-12
			hh=str(hh)
			tim=hh+":"+mm+" pm"
		elif hh==24:
				tim="00:"+mm+" am"
		else:
			tim=str(hh)+":"+str(mm)+" am"
		#print text
		print tim
		tim="The Time is "+tim
	os.system('/home/pi/April_mark_6_linux_version/./speak.sh "'+tim+'"')

def day_day():
	text=list(time.ctime().split(' '))
	day_s=['Mon','Tue','Wed','Thu','Fri','Sat','Sun'];
	day=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
	month_s=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
	month=['January','February','March','April','May','June','July','August','September','Octber','November','December']
	if text[2]!='':
		year=text[4]
		date=text[2]
		ti=list(text[3].split(':'))
		#print time[0],time[1],time[2]
		hh=ti[0]
		mm=ti[1]
		ss=ti[2]
		#if hh >12 and hh!=24:
		#    hh=int(hh)-12
		#    print hh,":",mm," pm"
		#elif hh==24:
		#        print "00:",mm," am"
		#else:
		#    print hh,":",mm," am"
		#print text
		d=day[day_s.index(text[0])]
		print d
		t="It's "+d
	else:
		year=text[5]
		date=text[3]
		ti=list(text[4].split(':'))
		#print time[0],time[1],time[2]
		hh=ti[0]
		mm=ti[1]
		ss=ti[2]
		#if hh >12 and hh!=24:
		#    hh=int(hh)-12
		#    print hh,":",mm," pm"
		#elif hh==24:
		#        print "00:",mm," am"
		#else:
		#    print hh,":",mm," am"
		#print text
		d=day[day_s.index(text[0])]
		print d
		t="It's "+d
	os.system('/home/pi/April_mark_6_linux_version/./speak.sh "'+t+'"')
