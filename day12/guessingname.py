from art import logo
import random

# generate a random number between 1 a 100
print(logo)

print("I'm thinking of a number between 1 and 100")

random_number = random.randrange(0, 101)
print(random_number)

user_difficulty = input(f"Choose a difficulty. Type 'easy' or hard: ")

user_chances = 0

if user_difficulty == 'easy':
    user_chances = 10
else:
    user_chances = 5

print(f"You have {user_chances} attempts remaining to guess the number")

user_number = 0


def compare(user, bot):
    if user > bot:
        print("Too high.")
    else:
        print("Too low.")


while user_number != random_number:
    while True:
        try:
            user_number = int(input("Make a guess: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    if user_number == random_number:
        print(f"You got it!. The answer was {random_number}.")
        break
    user_chances -= 1
    compare(user_number, random_number)
    print("Guess again.")
    print(f"You have {user_chances} attempts remaining to guess the number. ")
    if user_chances == 0:
        print("You've run out of a guesses, you lose")
        break












# 2 types of difficulty, if easy = 10 chances, hard = 5 chances

# if the user guess the wrong number, print the remaining chances and if the guessed number is higher or lowest of the random number

# if the guesses number its equal to the random number, the user win