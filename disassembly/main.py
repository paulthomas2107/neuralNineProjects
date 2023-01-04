import dis


def hello_world():
    msg = "Hello, Paul"
    return msg


def add(x, y, z):
    return x + y + z


# print(dis.dis(hello_world))
print(dis.dis(add))
