

import socket
host = "127.0.0.2" #Server address
port = 20610 #Port of Server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port)) #bind socket to network addr
s.listen(2)

#conn is client socket (connection)
#addr is IP/Port numbers
conn, addr = s.accept()

print "Server is on ", conn, addr

index = 0
str1 = "blankNow"
while str1 != "exit":
	index += 1
	#print addr, "Now Connected"
	conn.send("From server index number is: " + str(index))
	str1 = conn.recv(1024)
	print str1

	if index > 25:
		break
conn.close()