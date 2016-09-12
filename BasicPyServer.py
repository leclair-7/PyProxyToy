import socket
host = "192.168.99.101" #Server address
port = 20602 #Port of Server
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
	conn.send("From End server index #: " + str(index) +" BAM!")
	str1 = conn.recv(1024)
	
	print str1

	if index > 25:
		break
conn.send("exit")
conn.close()
