import ctypes

a = 10
b = 10

print(id(a), id(b))

a1 = [1, 2, 3]
b1 = a1
b1[0] = 100
print(a1)

c = ctypes.c_int(200)
print(c)
print(c.value)
print(type(c.value))
print(type(c))

d = ctypes.c_long(100)
ptr = ctypes.pointer(d)
print(ptr)
print(type(ptr))
print(ptr.contents)
print(ptr.contents.value)
print(ctypes.addressof(ptr.contents))
ptr.contents.value = 166
print(ctypes.addressof(ptr.contents))
print(d)
ptr_address = ctypes.addressof(ptr.contents)
ptr_new = ctypes.cast(ptr_address, ctypes.POINTER(ctypes.c_long))
print(ptr_new.contents.value)
