from multiprocessing import Pool, cpu_count
from threading import Timer
import time

def func1():
    print("hello")

def func2():
    print("goodbye")

def schedule(f, n):
    t = Timer(n/1000.0, f)
    t.start()

if __name__ == "__main__":
    schedule(func1, 1000)
    schedule(func2, 3000)