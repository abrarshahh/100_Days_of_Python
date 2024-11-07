#pick the person to pay the bill
import random

name_string = input("Write the name of people (seperate each name by a comma followed by a space): ")
names = name_string.split(", ")

random_name = random.choice(names)

print (random_name + " is going to buy the meal today!")