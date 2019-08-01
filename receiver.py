def goLive():
    #client portion
    import socket

    r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = socket.gethostname()
    port1 = 1237
    port2 = 1239

    r.connect((host, port1))
    message = r.recv(1024)
    print("RECEIVER | Packet received | ", end = "")
    print(message.decode("utf-8"))
    r.close()

    r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    r.connect((host, port2))
    message = r.recv(1024)
    print("RECEIVER | Packet received | ", end = "")
    print(message.decode("utf-8"))
    r.close()

