#armstrong number
value=int(input("enter a nuber")) #Enter a number
i=len(str(value)) #lenth of the input number
sum=0
temp=value

while value > 0:
    rem=value%10
    value=value//10
    multiply=rem**i
    sum=sum+multiply

if sum==temp:
    print(f"{temp}is a armstrong number")
else:
    print(f"{temp} is not a armstrong number")

