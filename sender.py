def goLive():
    import socket

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = socket.gethostname()
    port = 1234

    s.bind((host, port))
    s.listen(5)

    while True:
        clientsocket, address = s.accept()
        print(f"SENDER | Connected to {address}")
        clientsocket.send(bytes("<packet contents>", "utf-8"))
        clientsocket.close()
