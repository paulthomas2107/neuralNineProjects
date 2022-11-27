import socket
import struct


first_name = "Rory"
last_name = "Thomas"
age = 19
gender = 'M'
occupation = "Retail"
weight = 90.12

data = struct.pack("10s 15s i s 15s f",
                   first_name.encode(),
                   last_name.encode(),
                   age,
                   gender.encode(),
                   occupation.encode(),
                   weight)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))
client.send(data)
client.close()
