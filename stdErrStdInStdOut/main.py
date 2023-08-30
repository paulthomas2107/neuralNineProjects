import sys
import time

print("Hello World")
sys.stdout.write("Hello Paul\n")
sys.stderr.write("This is an error\n")
print("An error", file=sys.stderr)

# print(sys.stdin.read())
#  python main.py < file.txt


def progress_bar(total):
    sys.stdout.write("[")
    for i in range(total):
        time.sleep(0.1)
        sys.stdout.write("#")
        sys.stdout.flush()
    sys.stdout.write("]\n")


print(progress_bar(50))