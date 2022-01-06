from art import logo
import random

print(logo)
print("I'm thinking of a number between 1 and 100")
user_chances = 0


def difficulty():
    global user_chances
    user_difficulty = ''
    while user_difficulty != 'easy' or user_difficulty != 'hard':
        user_difficulty = str(input(f"Choose a difficulty. Type 'easy' or hard: "))
        if user_difficulty == 'easy':
            user_chances = 10
            break
        elif user_difficulty == 'hard':
            user_chances = 5
            break
        else:
            print("Oops! Type a valid difficulty, 'easy' or 'hard'.  Try again...")


def compare(user, bot):
    if user > bot:
        print("Too high.")
    else:
        print("Too low.")


def game():
    global user_chances
    print(f"You have {user_chances} attempts remaining to guess the number")
    user_number = 0
    random_number = random.randrange(0, 101)
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
        if user_chances == 0:
            print("You've run out of a guesses, you lose")
            break
        compare(user_number, random_number)
        print("Guess again.")
        print(f"You have {user_chances} attempts remaining to guess the number. ")


difficulty()
game()
