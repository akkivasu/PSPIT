#client portion
import socket

ps1A = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
portA = 1234

ps1A.connect((host, portA))

message = ps1A.recv(1024)
print(message.decode("utf-8"))

#server portion
ps1B = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

portB = 1235

ps1B.bind((host, portB))
ps1B.listen(5)

while True:
    clientsocket, address = ps1B.accept()
    print(f"Connected to {address}")
    clientsocket.send(bytes("<packet contents>", "utf-8"))
    clientsocket.close()
