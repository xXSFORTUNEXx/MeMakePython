import socket
import time

serversocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

host = socket.gethostname()
print ( "Hostname: ", host)

port = 9999
print ( "Port: ", port)

serversocket.bind( (host, port) )
serversocket.listen(5)
print ("Socket bind complete...\nListening for connections..." )

while True:
    clientsocket, addr = serversocket.accept()

    print ( "Connection from: ", addr)
    currentTime = time.ctime(time.time())
    clientsocket.send( currentTime.encode("ascii") )
    tm = clientsocket.recv(1024)
    message = tm.decode("ascii")

    if (message == "Close Socket"):
        print ( "Closing socket..." )
        clientsocket.close()