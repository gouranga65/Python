# armstrong number
# 1^3 + 5^3 + 3^3 = 153

num = int(input("Enter a num ::: "))  
temp = num              # BACKUP THE VALUE OF USER INPUT
digit = len(str(num))   # FIND THE LEN/DIGIT
res = 0                 # STORE THE RESULT

while num > 0:
    rem = num % 10      # FIND THE LAST DIGIT
    num = num // 10
    res = res + (rem ** digit)  # FIRST POWER, THEN SAVE THE VAL IN RES

if res == temp:         # CHECK IF THE RES AND NUM ARE SAME OR NOT
    print("Armstrong Number")
else:
    print("Not a Armstrong Number.")
