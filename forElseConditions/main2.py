import sys
import threading
import time

done = False


def end_loop():
    global done
    input("Press enter to terminate loop...\n")
    done = True


threading.Thread(target=end_loop).start()

for i in range(10):
    print(i)
    if done:
        break
    time.sleep(1)
else:
    print("Loop ended without intervention")
    sys.exit()
