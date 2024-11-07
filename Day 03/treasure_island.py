#tresure island

print(r'''         
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
                    \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |===|o|=======.'.'^'.'.========|o|===|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
  
  ''')


print("Welcome to 'Treasure Island'.\nYour goal is to find the treasure.")

print("You're at the beach. Which way will you go?")
direction = input("Type 'Front' , 'Back' , 'Right' , 'Left' :\n")

#choosing direction
if direction == "Front" :
    print("You've reached a mountain. This is a dead end. \nGAME OVER")
elif direction == "Back" :
    print("You gave up on your quest. \nGAME OVER.")
elif direction == "Right" :
    print("You encountered a wild animal. \nGAME OVER.")
elif direction == "Left" :
    print("You've reached a Lake. \nWould you Swim across the lake or Wait for a boat.")
    crossing = input("Type 'Swim' or 'Wait' : \n ")
  
#choosing how to cross lake
    if crossing == "Swim" :
      print("You encountered a crocodile. \nGAME OVER.")
    elif crossing == "Wait" :
      print("You've crossed the lake without any harm. \nThere are three doors in front of you ('Red' , 'Blue' and 'Yellow'). \nChoose one door.")
      door = input("Type 'Red' , 'Blue' or 'Yellow' : \n")

#choosing door
      if door == "Red" :
        print("You've encountered a Snake. \nGAME OVER.")
      elif door == "Blue" :
        print("There was a Deep Pit. \nGAME OVER.")
      elif door == "Yellow" :
        print("You've found the Treasure. \nCongratulations. \nYOU WIN.")
        
      else :
        print("No Such Door Exist. \nSTART OVER.")
        
    else :
      print("Invalid Action. \nSTART OVER.")
      
else :
    print("Invalid Direction. \nSTART OVER.")