
def goLive():
    #client portion
    import socket

    pr1A = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = socket.gethostname()
    port = 1235

    pr1A.connect((host, port))

    message = pr1A.recv(1024)
    print("PSEUDO-RECEIVER-1 | Packet received | ", end = "")
    print(message.decode("utf-8"))

    #server portion
    pr1B = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    portB = 1237

    pr1B.bind((host, portB))
    pr1B.listen(5)

    while True:
        clientsocket, address = pr1B.accept()
        print(f"PSEUDO-RECEIVER-1 | Connected to {address}")
        clientsocket.send(bytes("<packet contents>", "utf-8"))
        clientsocket.close()