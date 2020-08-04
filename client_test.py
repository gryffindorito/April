import socket
import time
s=socket.socket()
host='192.168.1.50'
port=1234
s.connect((host,port))
string="0110"
print "light on"
s.send(string)
s.close()
time.sleep(4)
s=socket.socket()
s.connect((host,port))
string="0111"
print "lights off"
s.send(string)
s.close()
