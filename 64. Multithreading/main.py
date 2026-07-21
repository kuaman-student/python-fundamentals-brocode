# multithreading = Used to perform multiple tasks concurrently (multitasking)

# Good for I/O bound tasks like reading files or fetching data from APIs threading.Thread(target-my_function)

import threading, time

def walk():
    time.sleep(1)
    print("Walked")

def eat(name):
    time.sleep(4)
    print(f"{name} Ate")

def study(fname, lname):
    time.sleep(7)
    print(f"{fname} {lname} Studied")

work1 = threading.Thread(target=walk)
work1.start()
work2 = threading.Thread(target=eat,args=("aman", ))
work2.start()
work3 = threading.Thread(target=study, args=("aman", "kumar"))
work3.start()

work1.join()
work2.join()
work3.join()
print("All work done")