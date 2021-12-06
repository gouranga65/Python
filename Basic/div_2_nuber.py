#divisable by 7 and multiple of 5
print=("enter a number between 1500 and 2700:: ")
n=int(input())
if(n%7==0):
    if(n%5==0):
        print(f"{n}is divisable by 7 and 5 ")
else:
    print("not divisable by 5 and 7")
    