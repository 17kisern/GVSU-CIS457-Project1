import socket                   # Import socket module

socketObject = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60000                    # Reserve a port for your service.

socketObject.connect((host, port))
socketObject.send(b"Hello Server!")

with open('ReceivedFile.txt', 'wb') as receivedFile:
    print("Successfully opened/created 'ReceivedFile.txt'")
    while True:
        print('Receiving data from server...')
        data = socketObject.recv(1024)
        print("Data Received: '%s'", (data))
        if not data:
            break
        # Write data to a file
        receivedFile.write(data)

receivedFile.close()
print("Successfully received and saved file")
socketObject.close()
print("Connection with Server Closed")
