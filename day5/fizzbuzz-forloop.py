# You are going to write a program that automatically prints the solution to the FizzBuzz game.
# https://en.wikipedia.org/wiki/Fizz_buzz

for user_number in range(1, 101):
    if user_number % 5 == 0 and user_number % 3 == 0:
        print("FizzBuzz")
    elif user_number % 3 == 0:
        print("Fizz")
    elif user_number % 5 == 0:
        print("Buzz")
    else:
        print(user_number)