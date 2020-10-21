import socket                               # Import socket module

"""

Notes
==============

socket.gethostname() gets the current machines hostname, for example "DESKTOP-1337PBJ"

bytes.decode("utf-8") decodes some 'bytes' object using the utf-8 standard that information gets sent over the internet in

all the b'string here' are converting a string into binary format. Hence the B

"""

socketObject = socket.socket()              # Create a socket object
host = socket.gethostname()                 # Get local machine name
port = 60000                                # Reserve a port for your service.
bufferSize = 1024

socketObject.connect((host, port))
socketObject.send(b"Hello Server!")

with open('ReceivedFile.txt', 'wb') as receivedFile:
    print("Successfully opened/created 'ReceivedFile.txt'")

    while True:
        print('Receiving data from server...')

        # Receiving data in 1 KB chunks
        data = socketObject.recv(bufferSize)

        # If there was no data in the latest chunk, then break out of our loop
        decodedString = data.decode("utf-8")
        if(decodedString == "\0" or not data):
            break

        print("Data Received: ", data.decode("utf-8"))

        # Write data to a file
        receivedFile.write(data)

receivedFile.close()
print("Successfully received and saved file")
socketObject.close()
print("Connection with Server Closed")
