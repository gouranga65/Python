
print("1. Press 1 for celcious to farenhight \n2. Press 2 for farenhight to celciuous")
user_input = int(input(">> "))

if user_input == 1:
    cel = int(input("Enter Celcious :: "))
    # Formula
    far = (cel * 9/5) + 32
    print(far)
elif user_input == 2:
    far = int(input("Enter Farenhight :: "))
    # Formula
    cel =(far-32)*5/9
    print(cel)
else:
    print("Wrong Input")
