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
    global connected
    global socketObject
    try:
        socketObject.connect((address, int(port)))
        print("\nSuccessfully connected to\nAddress: ", address, "\tPort: ", int(port))
        connected = True
    except:
        print("\nFailed to connect to\nAddress: ", address, "\tPort: ", int(port), "\nPlease Try Again")
        socketObject = socket.socket()
        connected = False

def Disconnect(commandArgs):
    global connected
    global socketObject
    try:
        command = " "
        socketObject.send(command.join(commandArgs).encode("UTF-8"))

        socketObject.close()
        socketObject = socket.socket()
        print("Successfully disconnected")
        connected = False
    except:
        print("Failed to disconnect! Please try again")
    return

def List(commandArgs):
    global socketObject
    
    command = " "
    socketObject.send(command.join(commandArgs).encode("UTF-8"))
    return

def Retrieve(commandArgs):
    return

def Store(commandArgs):
    return

def Quit(commandArgs):
    global socketObject
    
    Disconnect(commandArgs)
    return

def Shutdown_Server(commandArgs):
    global socketObject

    command = " "
    socketObject.send(command.join(commandArgs).encode("UTF-8"))
    return

def Main():
    print("You must first connect to a server before issuing any commands.")

    while True:
        userInput = input("\nEnter Command: ")
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

        if(commandGiven.upper() == "LIST" and len(commandArgs) == 1):
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
        elif(commandGiven.upper() == "DISCONNECT"):
            print("User ran DISCONNECT")
            Disconnect(commandArgs)
            continue
        elif(commandGiven.upper() == "QUIT"):
            print("User ran QUIT")
            Quit(commandArgs)
            break
        elif(commandGiven.upper() == "SHUTDOWN_SERVER"):
            print("User ran SHUTDOWN_SERVER")
            Quit(commandArgs)
            break
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
print("Program Closing")