# year = int(input("What year do you want to know if its a leap?"))

year = 1989
if year % 4 == 0:
    if year % 100 != 0:
        print("Leap")
    elif year % 100 == 0:
        if year % 400 != 0:
            print("Not Leap")
        elif year % 400 == 0:
            print("Leap year.")
else:
    print("Not leap year.")

