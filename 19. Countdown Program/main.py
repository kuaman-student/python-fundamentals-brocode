import time
myTime = int(input("Enter time in seconds:\t"))

while myTime <= 0:
    myTime = input("Enter correct time in seconds:\t")


for x in range(myTime, 0 , -1):
    sec = x%60
    minute = int(x/60)%60
    hour = int(x/3600)
    print(f"{hour:02}:{minute:02}:{sec:02}")
    time.sleep(1)





print("Your time is up!!")