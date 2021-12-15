# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height and tell them the interpretation of their BMI based.

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = int(weight) / float(height) ** 2

print(round(bmi, 1))

underweight = 18.5
normal_weight = 25
slightly_overweight = 30
obese = 35
bmi = float("{:.2f}".format(bmi))


#clinically_obese = True

if bmi < underweight:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < normal_weight:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < slightly_overweight:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < obese:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")