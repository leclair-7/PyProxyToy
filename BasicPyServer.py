

import socket
host = "127.0.0.1" #Server address
port = 20603 #Port of Server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port)) #bind socket to network addr
s.listen(2)

#conn is client socket (connection)
#addr is IP/Port numbers
conn, addr = s.accept()

print "Server is on ", conn, addr

index = 0
str1 = "blankNow"

proxStr = ""

while str1 != "exit":
	index += 1
	#print addr, "Now Connected"
	conn.send("From server index number is: " + str(index))

	#blocks/pauses here
	str1 = conn.recv(1024)
	if str1.split()[0].lower() == "pserver":
		conn.send("Enter <IPv4,port> to access from proxy:")
		proxStr = conn.recv(1024)
		while len(proxStr.split()) != 2:
			conn.send("Enter <IPv4,port> to access from proxy:")
			proxyStr = conn.recv(1024)
		p_host = proxyStr[0] # server address
		p_port = int(proxStr[1]) #server port
		proxy_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		proxy_sock.connect((p_host,p_port))

		msg_from_dest = ""

		backToStart = ""

		while msg_from_dest != "exit":
			proxy_sock.send("online,...")
			msg_from_dest = proxy_sock.recv(1024)
			conn.send(msg_from_dest)




		#now we'll access a server from a client socket

	print str1

	if index > 25:
		break
conn.close()