import socket

s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

host = socket.gethostname()
print ( "Hostname: ", host)

port = 9999
print ( "Port: ", port)

s.connect( (host, port))

tm = s.recv(1024)

print ("The time from the server is %s" % tm.decode("ascii"))

message = "Close Socket"

s.send(message.encode("ascii"))

s.close()