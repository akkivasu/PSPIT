import socket

#client portion
ps2A = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
portA = 1234

ps2A.connect((host, portA))

message = ps2A.recv(1024)
print(message.decode("utf-8"))

#server portion
ps2B = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

portB = 1236

ps2B.bind((host, portB))
ps2B.listen(5)

while True:
    clientsocket, address = ps2B.accept()
    print(f"Connected to {address}")
    clientsocket.send(bytes("<packet contents>", "utf-8"))
    clientsocket.close()
