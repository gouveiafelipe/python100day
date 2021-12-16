import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_answer = 0    # int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))


possibilities = [rock, paper, scissors]

print(possibilities[user_answer])

print(random_choice)
