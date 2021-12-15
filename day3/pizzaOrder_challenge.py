# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
print("Welcome to Python Pizza Deliveries!!")

#pizza's price

size = input("What size pizza do you want? S, M or L ?")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

small_price = 15
medium_price = 20
large_price = 25

small_size = "S"
medium_size = "M"
large_size = "L"

extra_pp_small = 2
extra_pp_medium_large = 3
order_cheese = 1

bill = 0

if size == small_size:
    bill += small_price
elif size == medium_size:
    bill += medium_price
bill += large_price

if add_pepperoni == "Y":
    if size == small_size:
        bill += extra_pp_small
    bill += extra_pp_medium_large

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
