from flask import Flask, render_template, Response,stream_with_context,request,json,jsonify
from camera import VideoCamera
#from audio_get import *
import socket               
import RPi.GPIO as GPIO 
import time
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)#right
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)#right
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)#left 
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)#left

data=[""]
app = Flask(__name__)
ip="192.168.1.36"
@app.route('/')
def index():
	text="Bot Controls"
	return render_template('controls.html',ip=ip,text=text)
		    
#Bot Controls		    
@app.route('/camerac1', methods=['GET', 'POST'])
def camerac1():
	print "Forward"
	data[0]="Done"
	GPIO.output(16, GPIO.HIGH)#a2
	GPIO.output(18, GPIO.LOW)#a1
	GPIO.output(13, GPIO.LOW)#b2
	GPIO.output(15, GPIO.HIGH)#b1
	return jsonify(data)
	"""
	    global er
	    s = socket.socket()         # Create a socket object
	    ##host = socket.gethostname() # Get local machine name
	    host="192.168.100.14"
	    port = 1234                # Reserve a port for your service.
	    s.connect((host, port))
	    ###print s.recv(1024)
	    inp="1"
	    s.send(str(inp))
	    d=s.recv(1024)
	    if d=="100":
		er="Obstacle in front"
	    elif d=="200":
		er="left collision"
	    elif d=="300":
		er="right collision"
	    s.close                     # Close the socket when done
	    #data = {}
	    #data['dat'] = inp
	    data={}
	    data['dat']=er
	    return jsonify(data)
	"""

@app.route('/camerac2', methods=['GET', 'POST'])
def camerac2():
	print "Left"
	data[0]="Done"
	GPIO.output(16, GPIO.HIGH)#a2
	GPIO.output(18, GPIO.LOW)#a1
	GPIO.output(13, GPIO.HIGH)#b2
	GPIO.output(15, GPIO.LOW)#b1
	return jsonify(data)
	"""
	    global er
	    s = socket.socket()         # Create a socket object
	    #host = socket.gethostname() # Get local machine name
	    host="192.168.100.14"
	    port = 1234                # Reserve a port for your service.
	    s.connect((host, port))
	    ##print s.recv(1024)
	    inp="4"
	    s.send(str(inp))
	    d=s.recv(1024)
	    if d=="100":
		er="Obstacle in front"
	    elif d=="200":
		er="left collision"
	    elif d=="300":
		er="right collision"
	    s.close                     # Close the socket when done
	    #data = {}
	    #data['dat'] = inp
	    data=er
	    print data
	    return jsonify(data)
	"""

@app.route('/camerac3', methods=['GET', 'POST'])
def camerac3():
	print "Right"
	data[0]="Done"
	GPIO.output(16, GPIO.LOW)#a2
	GPIO.output(18, GPIO.HIGH)#a1
	GPIO.output(13, GPIO.LOW)#b2
	GPIO.output(15, GPIO.HIGH)#b1
	return jsonify(data)
	"""
	    global er
	    s = socket.socket()         # Create a socket object
	    #host = socket.gethostname() # Get local machine name
	    host="192.168.100.14"
	    port = 1234                # Reserve a port for your service.
	    s.connect((host, port))
	    ##print s.recv(1024)
	    inp="3"
	    s.send(str(inp))
	    d=s.recv(1024)
	    if d=="100":
		er="Obstacle in front"
	    elif d=="200":
		er="left collision"
	    elif d=="300":
		er="right collision"
	    s.close                     # Close the socket when done
	    #data = {}
	    #data['dat'] = inp
	    data=er
	    print data
	    return jsonify(data)
	"""

@app.route('/camerac4', methods=['GET', 'POST'])
def camerac4():
	print "Reverse"
	data[0]="Done"
	GPIO.output(16, GPIO.LOW)#a2
	GPIO.output(18, GPIO.HIGH)#a1
	GPIO.output(13, GPIO.HIGH)#b2
	GPIO.output(15, GPIO.LOW)#b1
	return jsonify(data)
	"""
	    global er
	    s = socket.socket()         # Create a socket object
	    #host = socket.gethostname() # Get local machine name
	    host="192.168.100.14"
	    port = 1234                # Reserve a port for your service.
	    s.connect((host, port))
	    #print s.recv(1024)
	    inp="2"
	    s.send(str(inp))
	    d=s.recv(1024)
	    if d=="100":
		er="Obstacle in front"
	    elif d=="200":
		er="left collision"
	    elif d=="300":
		er="right collision"
	    s.close                     # Close the socket when done
	    #data = {}
	    #data['dat'] = inp
	    data=er
	    print data
	    return jsonify(data)
	"""

@app.route('/camerac5', methods=['GET', 'POST'])
def camerac5():
	print "Stop"
	data[0]="Done"
	GPIO.output(16, GPIO.LOW)#a2
	GPIO.output(18, GPIO.LOW)#a1
	GPIO.output(13, GPIO.LOW)#b2
	GPIO.output(15, GPIO.LOW)#b1
	return jsonify(data)
	"""
	    global er
	    s = socket.socket()         # Create a socket object
	    #host = socket.gethostname() # Get local machine name
	    host="192.168.100.14"
	    port = 1234                # Reserve a port for your service.
	    s.connect((host, port))
	    #print s.recv(1024)
	    inp="5"
	    s.send(str(inp))
	    d=s.recv(1024)
	    if d=="100":
		er="Obstacle in front"
	    elif d=="200":
		er="left collision"
	    elif d=="300":
		er="right collision"
	    s.close                     # Close the socket when done
	    #data = {}
	    #data['dat'] = inp
	    data=er
	    print data
	    return jsonify(data)
	"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=6060)
