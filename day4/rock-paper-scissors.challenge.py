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

user_answer = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))

print(f"You chose: {user_answer}")

draw = [[0, 0], [1, 1], [2, 2]]
win = [[0, 2], [1, 0], [2, 1]]
lose = [[0, 1], [1, 2], [2, 0]]

# criando lista de possibilidades
possibilities = [rock, paper, scissors]

# passando com indice o input do usuario
print(possibilities[user_answer])

# criando uma escolha aleatorio
random_choice = random.randint(0, len(possibilities) - 1)

print("-------------------------------")

print(f"The machineeee chooose... {random_choice} {possibilities[random_choice]}")

result = [user_answer, random_choice]

draw_true = result == draw[0] or draw[1] or draw[2]
win_true = result == win[0] or win[1] or win[2]
lose_true = result == lose[0] or lose[1] or lose[2]

if draw_true == result:
    print("Its a draw, ty again. ")
elif lose_true:
    print("You lose buddy, don't even try again! ")
else:
    print("-------------------------------")
    print("You win!!!")

