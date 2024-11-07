#Love Calculator

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combine = name1 + name2
combineLower = combine.lower()

t = combineLower.count("t")
r = combineLower.count("r")
u = combineLower.count("u")
e = combineLower.count("e")
true = t + r + u + e

l = combineLower.count("l")
o = combineLower.count("o")
v = combineLower.count("v")
love = l + o + v + e

score = str(true) + str(love)
score = int(score)

if score < 10 or score > 90:
  print(f"Your score is {score}%, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"your score is {score}%, you are alright together.")
else:
  print(f"your score is {score}%.")