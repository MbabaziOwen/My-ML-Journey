import time


my_time = int(input("enter time in seconds "))

for x in range(1,my_time):
    print(x)
    time.sleep(1)


print("Time's up ")