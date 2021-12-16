# # 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ") # string

position = str(33)

#transforming the user's answer to a list for taking the index

column = int(position[0]) -1
row = int(position[1]) -1


map[row][column] = " X  "



print("---------------------------------")

print(f"{row1}\n{row2}\n{row3}")

