import struct


byte_stream = struct.pack("iii", 10, 20, 30)

print(byte_stream)
print(struct.calcsize("i"))

a, b, c = struct.unpack("iii", byte_stream)
print(a, b, c)

company_name = b"Paul Computers"
day, month, year = 1, 1, 2022
awesome = True

byte_stream = struct.pack("15s 3i ?", company_name, day, month, year, awesome)
print(byte_stream)
a, b, c, d, e, = struct.unpack("15s 3i ?", byte_stream)
print(a, b, c, d, e)
# Tuple
also = struct.unpack("15s 3i ?", byte_stream)
print(also[0])

with open("data", 'wb') as f:
    f.write(byte_stream)

with open("data", "rb") as f:
    data = f.read()

a, b, c, d, e, = struct.unpack("15s 3i ?", data)
print(a, b, c, d, e)
