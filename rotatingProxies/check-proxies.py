import threading
import queue
import requests

q = queue.Queue()
valid_proxies = []

with open("output.txt", "r") as f:
    proxies = f.read().split("\n")
    for p in proxies:
        q.put(p)


def check_proxies():
    print("Started...")
    global q
    while not q.empty():
        proxy = q.get()
        print(proxy)
        try:
            res = requests.get("http://ipinfo.io/json",
                               proxies={"http": proxy,
                                        "https": proxy})
        except:
            continue
        if res.status_code == 200:
            print("passed...." + proxy)

    print("Ended...")


check_proxies()
