


t = "luca 3453.345.453.54 20602"
print t.split()
cat = 90
try:
	cat = int(t.split()[2])
except Exception:
	print("bad port number")


