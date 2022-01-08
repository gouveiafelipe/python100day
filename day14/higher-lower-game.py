from game_data import data
from art import logo
import random


def compare():
    total_score = 0  # variable to track the user's score
    play = True  # variable for the while loop run until the user lose the game

# picking a random number  from the dictionary of the list 'data' that represent a 'instagram account' and making a
    # new list with the values
    a = list(data[random.randint(0, len(data) - 1)].values()) # a represents an user/account
    b = list(data[random.randint(0, len(data) - 1)].values()) # b represents an user/account

# creating the variable tha will store the amount of followers from the variable above
    followers_a = a[1]
    followers_b = b[1]
    while play:
        print(f"Compare A: {a[0]}, a {a[2]}, from {a[3]}. ---- followers {a[1]}")
        print(logo)
        print(f"Against B: {b[0]}, a {b[2]}, from {b[3]}. ---- followers {b[1]}")
        user_guess = input("Who has more followers? Type 'A' or 'B'").lower()
        if user_guess == 'a' and followers_a > followers_b: # checking the user's answers
            play = True
            total_score += 1
            b = list(data[random.randint(0, len(data) - 1)].values())
            followers_b = b[1]
        elif user_guess == 'a' and followers_a < followers_b:
            play = False
        elif user_guess == 'b' and followers_b > followers_a: # checking the user's answers
            play = True
            total_score += 1
            a = b  # if the correct answer is B, we'll replace the variable A with the B's information.
            followers_a = followers_b  # if the correct answer is B, we'll replace the followers of variable A with
            # the B's information.
            b = list(data[random.randint(0, len(data) - 1)].values()) # picking another user/account from the list
            followers_b = b[1]
        else:
            play = False

    print(f"You loooose!! Your total score is: {total_score}")


compare()

