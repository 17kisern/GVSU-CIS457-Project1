import os
import socket                   # Import socket module
import asyncio

port = 60000                    # Reserve a port for your service.
maxConnections = 5
bufferSize = 1024
queueShutdown = False
activeConnections = []

"""

Notes
==============

socket.gethostname() gets the current machines hostname, for example "DESKTOP-1337PBJ"

string.encode('UTF-8') encodes the given string into a 'bytes' literal object using the utf-8 standard that is required
bytes.decode("utf-8") decodes some 'bytes' object using the utf-8 standard that information gets sent over the internet in

all the b'string here' are converting a string into binary format. Hence the B

asyncio is just a library that allows us to run parallel operations without stressing about all the bullshit that comes with multithreading. It allows us to run multiple connections simultaneously

"""


def List(connection, commandArgs):
    return

def Retrive(connection, commandArgs):
    connectionAddress = connection[1]
    connectionSocket = connection[0]

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
    return

def Store(connection, commandArgs):
    return

def ShutdownConnection(connection):
    global activeConnections
    connectionAddress = connection[1]
    connectionSocket = connection[0]

    print("[", connectionAddress, "] Ending Connection")

    # # For every send from one device, we need to have another device listening otherwise the program will hang
    # connectionSocket.send(b"Thank you for connecting")
    connectionSocket.close()
    activeConnections.remove(connection)

def ShutdownServer():
    global activeConnections
    global queueShutdown

    for connection in activeConnections:
        ShutdownConnection(connection)
    queueShutdown = True
    return

async def ManageConnection(connection):
    connectionAddress = connection[1]
    connectionSocket = connection[0]
    print("[", connectionAddress, "] Received Connection")

    while True:
        data = connectionSocket.recv(1024)
        commandGiven = data.decode("UTF-8")
        commandArgs = commandGiven.split()

        print("[", connectionAddress, "] Received Command: ", commandGiven)

        if(commandGiven.upper() == "LIST" and len(commandArgs) == 1):
            List(connection, commandArgs)
            continue
        elif(commandGiven.upper() == "RETRIEVE"):
            Retrieve(connection, commandArgs)
            continue
        elif(commandGiven.upper() == "STORE"):
            Store(connection, commandArgs)
            continue
        elif(commandGiven.upper() == "QUIT" or commandGiven.upper() == "DISCONNECT"):
            # Close this connection
            ShutdownConnection(connection)
            break
        elif(commandGiven.upper() == "SHUTDOWN_SERVER"):
            ShutdownConnection(connection)
            ShutdownServer()
            break
        else:
            print("Invalid Command Received.")
            connectionSocket.send(b"Invalid Command. Please Try Again.")
            connectionSocket.send(b"\0")
            continue


def Main():
    # Create a socket object
    openSocket = socket.socket()

    # Get local machine name
    # host = socket.gethostname()
    host = "localhost"

    # Bind to the port
    openSocket.bind((host, port))

    # Configure to allow 5 connections
    openSocket.listen(maxConnections)

    # Wait for new connections
    while True:
        # print("Number of Connections: ", numConnections)
        # [connectionSocket, connectionAddress]
        print("Awaiting Connection")
        if not queueShutdown:
            tupleboi = openSocket.accept()
            global activeConnections
            activeConnections.append(tupleboi)
            asyncio.run(ManageConnection(tupleboi))
        else:
            break

Main()
print("Program Closing")