

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1" # server address
port =20603 #server port
s.connect((host,port))

index = 25
while True:
	index += 1
	print s.recv(1024)	
	str1 = raw_input("insert next thing to send")
	s.send( str1+": " + str(index))
	

	if index > 50:
		break
s.close()