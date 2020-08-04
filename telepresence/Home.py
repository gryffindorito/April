from flask import Flask, render_template, Response,stream_with_context,request,json,jsonify
from camera import VideoCamera
#from audio_get import *
import socket               

data=[""]
app = Flask(__name__)
ip="192.168.1.40"
host='192.168.1.50'
port=1234
@app.route('/')
def index():
	text="Home Automation"
	return render_template('Home.html',ip=ip,text=text)
		    
#Bot Controls		    
@app.route('/On', methods=['GET', 'POST'])
def On():
	print "Light On"
	s=socket.socket()
	s.connect((host,port))
	string="0111"
	print "light on"
	s.send(string)
	s.close()
	data[0]="Done"
	return jsonify(data)
	
@app.route('/Off', methods=['GET', 'POST'])
def Off():
	print "Light Off"
	s=socket.socket()
	s.connect((host,port))
	string="0110"
	print "light off"
	s.send(string)
	s.close()
	data[0]="Done"
	return jsonify(data)
	
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)
