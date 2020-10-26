import socket                               # Import socket module

"""

Notes
==============

socket.gethostname() gets the current machines hostname, for example "DESKTOP-1337PBJ"

string.encode('UTF-8') encodes the given string into a 'bytes' literal object using the utf-8 standard that is required
bytes.decode("utf-8") decodes some 'bytes' literal object using the utf-8 standard that information gets sent over the internet in

all the b'string here' are converting a string into binary format. Hence the B

"""

connected = False
socketObject = socket.socket()              # Create a socket object
# host = socket.gethostname()
# host = "localhost"                          # Get local machine name
# port = 60000                                # Reserve a port for your service.
bufferSize = 1024

def Connect(address, port: int):
    try:
        socketObject.connect((address, int(port)))
        print("Successfully connected")
        connected = True
    except:
        print("Failed to connect! Please try again")
        connected = False

def Disconnect(commandArgs):
    return

def List(commandArgs):
    return

def Retrieve(commandArgs):
    return

def Store(commandArgs):
    return

def Quit(commandArgs):
    return

def Main():
    print("You must first connect to a server before issuing any commands.")

    while True:
        userInput = input("Enter Command: ")
        commandArgs = userInput.split()
        commandGiven = commandArgs[0]

        if(commandGiven.upper() == "CONNECT" and len(commandArgs) == 3):
            if connected:
                Disconnect(commandArgs)
                Connect(commandArgs[1], commandArgs[2])
            else:
                Connect(commandArgs[1], commandArgs[2])
            continue
        else:
            if not connected:
                print("You must first connect to a server before issuing any commands.")
                continue

        if(commandGiven.upper() == "LIST"):
            print("User ran LIST")
            List(commandArgs)
            continue
        elif(commandGiven.upper() == "RETRIEVE"):
            print("User ran RETRIEVE")
            Retrieve(commandArgs)
            continue
        elif(commandGiven.upper() == "STORE"):
            print("User ran STORE")
            Store(commandArgs)
            continue
        elif(commandGiven.upper() == "QUIT"):
            print("User ran QUIT")
            Quit(commandArgs)
            continue
        else:
            print("Invalid Command. Please try again.")
            continue


        # socketObject.send(userInput.encode('UTF-8'))

        # with open('ReceivedFile.txt', 'wb') as receivedFile:
        #     print("Successfully opened/created 'ReceivedFile.txt'")

        #     while True:
        #         print('Receiving data from server...')

        #         # Receiving data in 1 KB chunks
        #         data = socketObject.recv(bufferSize)

        #         # If there was no data in the latest chunk, then break out of our loop
        #         decodedString = data.decode("utf-8")
        #         if(decodedString == "\0" or not data):
        #             break

        #         print("Data Received: ", data.decode("utf-8"))

        #         # Write data to a file
        #         receivedFile.write(data)

        # receivedFile.close()
        # print("Successfully received and saved file")
        # socketObject.close()
        # print("Connection with Server Closed")

Main()