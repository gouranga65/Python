# divisable by 7 and multiple of 5

start = 1500
stop = 2700

for i in range(start, stop + 1):
    if(i % 7 == 0) and (i % 5 == 0):
        print(i, end=" ")
