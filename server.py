import os
import socket                   # Import socket module
import asyncio

port = 60000                    # Reserve a port for your service.
numConnections = 5
bufferSize = 1024


def Main():
    # Create a socket object
    openSocket = socket.socket()

    # Get local machine name
    host = socket.gethostname()

    # Bind to the port
    openSocket.bind((host, port))

    # Configure to allow 5 connections
    openSocket.listen(numConnections)

    print('Server listening....')

    # Wait for new connections
    while True:
        # Start listening for an individual connection
        # [connectionSocket, connectionAddress]
        tupleboi = openSocket.accept()

        # Spin off a thread to handle this connection
        asyncio.run(ManageConnection(tupleboi))


async def ManageConnection(connection):
    connectionAddress = connection[1]
    connectionSocket = connection[0]

    # Create a header to be sent first
    header: bytes = 0

    while True:
        print("[", connectionAddress, "] Received Connection")
        data = connectionSocket.recv(1024)
        print("[", connectionAddress, "] Received data: ", data.decode("utf-8"))

        fileName = "OriginalFile.txt"
        fileSize = os.path.getsize(fileName)
        print("FileSize: ", fileSize)
        downloadRemaining = fileSize
        fileItself = open(fileName, "rb")

        # Breaking the file down into smaller data chunks
        fileInBytes: bytes = 0
        if(fileSize < bufferSize):
            fileInBytes = fileItself.read(fileSize)
        else:
            fileInBytes = fileItself.read(bufferSize)

        while fileInBytes:
            connectionSocket.send(fileInBytes)
            print("[", connectionAddress, "] Sent: ", fileInBytes.decode("utf-8"))

            if(downloadRemaining < bufferSize):
                fileInBytes = fileItself.read(downloadRemaining)
            else:
                fileInBytes = fileItself.read(bufferSize)

        # Let the client know we're done sending the file
        connectionSocket.send(b'\0')
        fileItself.close()

        print("[", connectionAddress, "] Ending Connection")

        connectionSocket.send(b"Thank you for connecting")
        connectionSocket.close()
        break

Main()
print("After Main")
