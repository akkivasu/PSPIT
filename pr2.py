#client portion
import socket

pr2A = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
portA = 1236

pr2A.connect((host, portA))

meassage = pr2A.recv(1024)
print(meassage.decode("utf-8"))

#server portion
pr2B = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

portB = 1238

pr2B.bind((host, portB))
pr2B.listen(5)

while True:
    clientsocket, address = pr2B.accept()
    print(f"Connected to {address}")
    clientsocket.send(bytes("<packet contents>", "utf-8"))
    clientsocket.close()
