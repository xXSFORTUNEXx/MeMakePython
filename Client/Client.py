import socket
import time
s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

host = socket.gethostname()
print ( "Hostname: ", host)

port = 9999
print ( "Port: ", port)

s.connect( (host, port))

tm = s.recv(1024)

print ("Server Time: %s" % tm.decode("ascii"))

message = "Close"
s.send(message.encode("ascii"))
s.close()