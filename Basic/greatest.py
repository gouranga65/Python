from ast import If


print('greatest among three numbers')
num1=int(input('enter 1st number :: '))
num2=int(input('enter 2nd number :: '))
num3=int(input('enter 3rd number :: '))
if (num1>num2): 
    print("%s is greater among three "%num1)
elif (num2>num3):
    print("%s is greater among three "%num2)
else:
    print("%s is greater among all "%num3)