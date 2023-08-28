import filelock
#  commandline: for i in {1..10}; do python3 app.py & done
lock = filelock.FileLock('counter.lock')

# lock.acquire()
# lock.release()

for _ in range(100):
    with lock:
        with open("counter.txt", 'r') as f:
            current = int(f.read())

        current += 1

        with open("counter.txt", 'w') as f:
            f.write(str(current))