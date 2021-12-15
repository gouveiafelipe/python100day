print(''' Welcome to Treasure Island.\n
Your mission is to find the treasure.
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/___/____
*******************************************************************************
''')

endgame1 = "It's a room full of fire. Game Over."
endgame2 = "You chose a door that doesn't exist. Game Over."
endgame3 = 'You enter a room of beasts. Game Over.'
endgame4 = "You get attacked by an angry trout. Game Over."
endgame5 = "You fell into a hole. Game Over."
win = "You found the treasure! You Win!"

choice1 = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"').lower()

left = "left"
right = "right"


if choice1 == left:
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait"'
                    ' to wait for a boat. Type "swim" to swim across.').lower()
    if choice2 == "wait":
        choice3 = input('You arrive at the island unharmed. There is a house with 3 doors.'
                        ' One red, one yellow and one blue. Which colour do you choose?').lower()
        if choice3 == "yellow":
            print(win)
        elif choice3 == "red":
            print(endgame1)
        elif choice3 == "blue":
            print(endgame3)
    else:
        print(endgame4)
else:
    print(endgame5)



