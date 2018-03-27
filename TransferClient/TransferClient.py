import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60000                    # Reserve a port for your service.

s.connect((host, port))
message = "Hello Server!"
s.send(message.encode('ascii'))

with open('received_file.txt', 'wb') as f:
    print ('file opened')
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data= ', data.decode('ascii'))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Successfully received the file')
s.close()
print('connection closed')