import time
import lzma
import gzip
import bz2

data = b'This is some sample data' * 100000

print("Original data size is: ", len(data))

start = time.time()
compressed_data_lzma = lzma.compress(data)
end = time.time()
print(end - start)
print(len(compressed_data_lzma))
print("==============================")
# print(lzma.decompress(compressed_data_lzma))

start = time.time()
compressed_data_gzip = gzip.compress(data, compresslevel=9)
end = time.time()
print(end - start)
print(len(compressed_data_gzip))
print("==============================")

start = time.time()
compressed_data_bz2 = bz2.compress(data)
end = time.time()
print(end - start)
print(len(compressed_data_bz2))
print("==============================")

with open('file.txt', 'rb') as f_in, lzma.open('file.xz', 'wb') as f_out:
    f_out.write(f_in.read())

with lzma.open('file.xz', 'rb') as f_in, open('uncompressed.txt', 'wb') as f_out:
    f_out.write(f_in.read())