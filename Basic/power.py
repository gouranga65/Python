num=int(input('enter your number'))
power=int(input('enter the range of powres'))
temp=1
for i in range(0,power):
    temp=num**i
    i+=1
    print(temp)
