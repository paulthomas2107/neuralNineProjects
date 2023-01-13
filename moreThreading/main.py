import threading
import time

done = False


def worker(text):
    counter = 0
    while not done:
        time.sleep(1)
        counter += 1
        print(f"{text}: {counter}")


threading.Thread(target=worker, daemon=True, args=("Rory", )).start()
threading.Thread(target=worker, daemon=False, args=("Caitlin", )).start()

input("Press Enter to quit")
done = True
