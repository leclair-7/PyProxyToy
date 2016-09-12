import socket
host = "192.168.99.101" #Server address
port = 20610 #Port of Server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port)) #bind socket to network addr
s.listen(2)

#conn is client socket (connection)
#addr is IP/Port numbers
conn, addr = s.accept()

#print "Server is on ", conn, addr
index = 0
str1 = "blankNow"

isProxyOn = False
sockToDest = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while str1 != "exit":
	index += 1
	#print addr, "Now Connected"
	conn.send("From middle server, msg#: " + str(index))
	str1 = conn.recv(1024)

	''' good part starts here'''

	# See if client sent right signal to use the proxy to go someplace else
	if isProxyOn is False and str1.split() != [] and str1.split()[0] == "prox" and len(str1.split()) is 3:
		dest_ip = str1.split()[1]
		try:		
			dest_port = int( str1.split()[2] )			
			#now have dest_ip, dest_port
			
			print "ready for next hop"
			print( "[+] - Attempting connection with wanted destination" )
			sockToDest.connect((dest_ip,dest_port))
			isProxyOn = True
			print "[+] - We have proxy to end server connectivity"					
			
		except Exception:
			print "bad port number"
	elif isProxyOn is True:
		''' Potential for weirdness due to blocking errors'''		
		sockToDest.send(str1)
		msg_from_end = sockToDest.recv(1024)
		conn.send(msg_from_end)
	else:
		print str1	
		
		
	#print str1

	if index > 25:
		break
conn.send("exit")
conn.close()
sockToDest.close()
