'''list=[11,2,3,4,5,6]
max=list[0]
for i in list:
    if i>max:
        max=i
print(max)'''
 
num1=int(input('enter 1st number'))
num2=int(input('enter 2nd number'))
num3=int(input('enter 3rd number'))
if num1>num2 and num1>num3:
    print('num1')
elif num2>num1 and num2>num3:
    print('num2')
else:
    print('num3')