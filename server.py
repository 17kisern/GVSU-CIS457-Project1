import socket                   # Import socket module

port = 60000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print('Server listening....')

while True:
    connectionSocket, connectionAddress = s.accept()     # Establish connection with client.
    print("Received Connection from: ", connectionAddress)
    data = connectionSocket.recv(1024)
    print("Server received", repr(data))

    fileName = "OriginalFile.txt"
    fileItself = open(fileName, "rb")
    fileInBytes = fileItself.read(1024)
    while fileInBytes:
        connectionSocket.send(fileInBytes)
        print("Sent: ", repr(fileInBytes))
        fileInBytes = fileItself.read(1024)
    fileItself.close()

    print("Done sending")
    connectionSocket.send(b"Thank you for connecting")
    connectionSocket.close()
