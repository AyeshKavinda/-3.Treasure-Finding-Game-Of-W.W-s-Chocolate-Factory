#Interesting mind mapping play a game where you are hunting for the treasure of "W.W's Chocolate Factory". Good luck!
#Thanks to @Angela Yu, and @TheAppBrewery for the main model of the project. I have made my 3rd project with python.

print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Willy Wonka's Treasure Island.")
print("Your mission is to find the treasure of Willy Wonka's Chocolate Factory.") 

#You have multiple choices in order to make of difficulties of the game.

choice1 = input('You\'ve arrived to the land of willywonka! Where do you want to go? Type "left" or "right".\n').lower()

if choice1 == "left":
  choice2 = input('You have two options to cross the lake, Do you wish to wait for the boat or swim? Type "swim" or "wait".\n').lower()
  if choice2 == "wait":
    choice3 = input('You\'ve arrived the land of "Magic Factory"! Now there are 3 main doors "Red","Blue", and "Yellow", Which door do you wish to go inside?.\n').lower()
    if choice3 == "yellow":
     print('"Congratulations!"" You\'ve found the treasure of bars of "Willy Wonkas Chocolate"\n')
    elif choice3 == "red":
     print("You've turned into a cat with the help of wizard's spell, Game Over.")
    elif choice3 == "blue":
     print("Well done, you've fallen into the toxic acids of magic spells in the underground, Game Over.")
    else:
     print("Your answer doesn't exist, Game Over.")
  elif choice2 == "swim":
    print("You got biten by crocodiles!, Game Over.")
  else:
    print("Your answer doesn't exist, Game Over.")
elif choice1 == "right":
  print("You went to the haunted house, Game Over.")
else:
  print("Your answer doesn't exist, Game Over.")
    
  
  
      
