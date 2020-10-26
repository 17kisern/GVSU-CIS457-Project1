import os
import socket                   # Import socket module
import asyncio

port = 60000                    # Reserve a port for your service.
maxConnections = 5
bufferSize = 1024

"""

Notes
==============

socket.gethostname() gets the current machines hostname, for example "DESKTOP-1337PBJ"

string.encode('UTF-8') encodes the given string into a 'bytes' literal object using the utf-8 standard that is required
bytes.decode("utf-8") decodes some 'bytes' object using the utf-8 standard that information gets sent over the internet in

all the b'string here' are converting a string into binary format. Hence the B

asyncio is just a library that allows us to run parallel operations without stressing about all the bullshit that comes with multithreading. It allows us to run multiple connections simultaneously

"""


def Main():
    # Create a socket object
    openSocket = socket.socket()

    # Get local machine name
    host = socket.gethostname()

    # Bind to the port
    openSocket.bind((host, port))

    # Configure to allow 5 connections
    openSocket.listen(maxConnections)

    # Wait for new connections
    while True:
        # print("Number of Connections: ", numConnections)
        # [connectionSocket, connectionAddress]
        print("Awaiting Connection")
        tupleboi = openSocket.accept()

        asyncio.run(ManageConnection(tupleboi))


async def ManageConnection(connection):
    connectionAddress = connection[1]
    connectionSocket = connection[0]

    while True:
        print("[", connectionAddress, "] Received Connection")
        data = connectionSocket.recv(1024)
        print("[", connectionAddress, "] Received Command: ", data.decode("utf-8"))

        fileName = "OriginalFile.txt"
        fileItself = open(fileName, "rb")

        # Breaking the file down into smaller data chunks
        fileInBytes = fileItself.read(bufferSize)

        while fileInBytes:
            connectionSocket.send(fileInBytes)
            print("[", connectionAddress, "] Sent: ", fileInBytes.decode("utf-8"))

            fileInBytes = fileItself.read(bufferSize)

        # Let the client know we're done sending the file
        connectionSocket.send(b'\0')
        fileItself.close()

        print("[", connectionAddress, "] Ending Connection")

        # # For every send from one device, we need to have another device listening otherwise the program will hang
        # connectionSocket.send(b"Thank you for connecting")
        connectionSocket.close()
        break

Main()
print("After Main")
