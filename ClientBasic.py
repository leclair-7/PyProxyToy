

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.99.101" # server address
port =20610 #server port
s.connect((host,port))

index = 25
while True:
	index += 1
	fromServ =  s.recv(1024)
	print fromServ
	if fromServ == "exit":
		break
	str1 = raw_input("insert next thing to send: ")
	s.send( str1)
	

	if index > 50:
		break
s.close()
