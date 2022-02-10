year=int(input('enter your year'))
if year%4==0 and year%400==0:
    print(f'{year} is leap year')
else:
    print('not a leap year')