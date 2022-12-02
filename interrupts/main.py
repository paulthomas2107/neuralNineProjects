import signal
import time


def interrupt_handler(signum, frame):
    print("Trying to interrupt....")


signal.signal(signal.SIGINT, interrupt_handler)

while True:
    print("Hey...")

