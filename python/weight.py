'''weight=input('enter your weight in pound ')
b=0.45* int(weight)
print(b)
print("My name is %s" %'gouranga')
x='hello'
print("%s i am gouranga"%x)
print("i got %2.3d"%123456.543332)
value= 12
string = "Variable as integer = %d \n\
Variable as float = %f" %(value, value )
 
print (string)
clg='bcrec'
print(f"i read in {clg}")'''


weight=int(input('enter your weight:> '))
print('enter your choice no1  for lbs to kg and no2 kg to lbs')
option=int(input())
if option==1:
    kg=0.45*weight
    print(kg)
elif option==2:
    lbs=2.20*weight
    print(lbs)
else:
    print('andha hai kia lovde')