
import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print ('Connection: ', addr)
    currentTime = time.ctime(time.time())
    message = 'what up with that!'
    c.send(currentTime.encode('ascii'))
    c.send(message.encode('ascii'))
    c.close()