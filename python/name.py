name=len(input('enter your name:> '))
#print(name)
if name<3:
    print('name must be atleast 3 character')
elif name>50:
    print('name can be maximum of 50 char')
else:
    print('name is awesome')