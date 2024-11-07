#rock paper scissor
import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

images = [rock, paper, scissor]

print("Welcome to 'Rock Paper Scissor game.'")

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor: \n"))
bot_choice = random.randint(0,2)

if choice > 2 or choice < 0:
  print("Invalid Action!")

else :
  print(images[choice])
  print("Computer choose:")
  print(images[bot_choice])
  
  if choice == 0 and bot_choice == 2:
    print("You Win!")
  elif bot_choice == 0 and choice == 2:
    print("You Lose!")
  elif choice > bot_choice:
    print("You Win!")
  elif bot_choice > choice:
    print("You Lose!")
  elif choice == bot_choice:
    print("It's a tie!")