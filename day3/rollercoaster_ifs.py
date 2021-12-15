
print("Welcome to the rollercoaster!")
heigh = int(input("What is your heigh in cm? "))

age_range1 = 12
age_range2 = 18
ticket_tobe_paid = 0

if heigh >= 120:
    print("You can ride the rollercoaster!!")
    age = int(input("What is your age? "))

    if age < age_range1:
        ticket_tobe_paid = 5
        print("Child tickets are $5")
    elif age < age_range2:
        ticket_tobe_paid = 7
        print("Youth tickets are $7")
    else:
        ticket_tobe_paid = 12
        print("Adult tickets are $12")

    want_photo = input("Do you want a picture? Y or N. ")
    if want_photo == "Y":
        ticket_tobe_paid += 3
        print(f"The total bill is ${ticket_tobe_paid}")
    else:
        print(f"The total bill is ${ticket_tobe_paid}")
else:
    print("can't ride")