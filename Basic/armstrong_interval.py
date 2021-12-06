#armstrong withn a given range
num1=100
num2=500
add=0

for num in range(num1,num2+1):
    temp=num
    j=len(str(num))
    while num>0:
        rem=num%10
        num=num//10
        sum=rem**j
        add=add+sum
if temp==add:
    print("ok")
