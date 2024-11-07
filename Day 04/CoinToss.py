#Coin Toss
import random

print("Coin Toss.")
input("Press Enter to Toss the Coin.")
randomInt = random.randint(0,1)

if randomInt == 1:
  print("Heads")
else :
  print("Tails")