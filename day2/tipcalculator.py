# Project: tip calculator

print("Welcome to the tip calculator!\n")

total_bill = float(input("What was the total bill? $"))

tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

people_split = int(input("How many people to split the bill? "))

individual_bill = round((total_bill / people_split) * ((tip_percentage/100) + 1), 2)

individual_bill = "{:.2f}".format(individual_bill)

message = f"Each person should pay ${individual_bill}"

print(message)