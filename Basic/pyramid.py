num=int(input('enter rows'))
k=0
for i in range(1,num+1):
    for space in range(1, (num-i)+1):
        print(end="   ")

    while k!=(2*i-1):
        print("* ",end=" ")
        k+=1
    k=0
    print()