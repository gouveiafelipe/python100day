import random

# You are going to write a program that will select a random name from a list of names.
# The person selected will have to pay for everybody's food bill.
# Important: You are not allowed to use the choice() function.
names_string = input("Give me everybody's names, separated by a comma. ")

# changing the string in to a list
names = names_string.split(", ")

# get the total number of item in list.
people_count = len(names)

# random.randint function demands two parametres

random_nmr = random.randint(0, people_count - 1)

random_name = names[random_nmr]

print(f"{random_name} is going to pay the meal today!")

# random_name = random.randint()
