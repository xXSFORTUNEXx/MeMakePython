import socket

port = 60000
s = socket.socket()
host = socket.gethostname()
s.bind((host, port))
s.listen(5)

print ('Server listening....')

while True:
    conn, addr = s.accept()
    print ('Got connection from'), addr
    data = conn.recv(1024)
    print('Server received', data.decode('ascii'))

    filename='mytext.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Sent ',l.decode('ascii'))
       l = f.read(1024)
    f.close()

    print('Done sending')
    message = 'Thank you for connecting'
    conn.send(message.encode('ascii'))
    conn.close()
