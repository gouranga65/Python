start=int(input('enter number:> '))
stop=int(input('enter number'))
print('prime numbers are')
for i in range(2,stop):
	if i%2==0:
		print()
	else:
		print(i,end="")