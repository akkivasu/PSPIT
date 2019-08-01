def goLive():
    import socket

    #client portion
    ps2A = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = socket.gethostname()
    portA = 1235

    ps2A.connect((host, portA))

    message = ps2A.recv(1024)
    print("PSEUDO-SENDER-2 | Packet received | ", end = "")
    print(message.decode("utf-8"))

    #server portion
    ps2B = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    portB = 1236

    ps2B.bind((host, portB))
    ps2B.listen(5)

    while True:
        clientsocket, address = ps2B.accept()
        print(f"PSEUSO-SENDER-2 | Connected to {address}")
        clientsocket.send(bytes("<packet contents>", "utf-8"))
        clientsocket.close()
