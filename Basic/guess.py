scret=9
guess=0

while guess<3:
    user=int(input('enter THE SECRECT number:> '))
    if user==scret:
        print('done')
        break
    else:
        print('try again')
        
    guess+=1
