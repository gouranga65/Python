# armstrong withn a given range

# def isArmstrong(value):
#     i = len(str(value))  # lenth of the input number
#     sum = 0
#     temp = value

#     while value > 0:
#         rem = value % 10
#         value = value//10
#         multiply = rem**i
#         sum = sum+multiply

#     if sum == temp:
#         return True
#     else:
#         return False


# for i in range(100, 9999):
#     if isArmstrong(i) == True:
#         print(i, end=" ")


# NESTED LOOP

for num in range(100, 9999):
    temp = num
    i = len(str(num))
    sum = 0

    while num > 0:
        rem = num % 10
        num = num//10
        multiply = rem ** i
        sum = sum + multiply

    if sum == temp:
        print(sum, end=" ")
