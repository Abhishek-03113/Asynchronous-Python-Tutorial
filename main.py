import asyncio
import time
import requests
import threading
from threading import Thread


def infinite_loop():
    i = 0
    while i < 100000000:
        i += 1

    print("Counted to 100000")


def hello():
    print("Hello Abhishek")


t1 = Thread(target=infinite_loop)
t2 = Thread(target=hello)

t1.start()
t2.start()
