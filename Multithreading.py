import threading
import time

def func(seconds):
    print(f"Sleeping for {seconds} Seconds")
    time.sleep(seconds)

time1 = time.perf_counter()
# Normal Code
# func(5)
# func(2)
# func(1)

# Using Code
t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[1])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

time2 = time.perf_counter()
print(time2-time1)

