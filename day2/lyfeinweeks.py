# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x days, y weeks, and z months left

age = input("What is your current age? ")

#print(type(age))

age = 90 - int(age)
day = 365
week = 52
month = 12

days = age * day
weeks = age * week
months = age * month



print(f"You have {days} days, {weeks} weeks and {months} months left")
