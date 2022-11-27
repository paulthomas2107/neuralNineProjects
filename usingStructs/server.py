import socket
import struct

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))

server.listen()

client, addr = server.accept()

data = client.recv(1024)

first, last, age, gender, job, weight = struct.unpack("10s 15s i s 15s f", data)

print(first.decode().rstrip("\x00"),
      last.decode().rstrip("\x00"),
      age, gender.decode().rstrip("\x00"),
      job.decode().rstrip("\x00"),
      round(weight, 2))

server.close()
