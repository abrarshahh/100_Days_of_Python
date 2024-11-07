#Area calculaton
import math

def area(height,width,cover):
  cans = math.ceil( (height*width) / cover )
  print(f"Total number of cans needed are {cans}")

test_h = int(input("What is the height of wall(m)? \n"))
test_w = int(input("What is the width of wall(m)? \n"))
coverage = 5

area(height=test_h, width=test_w, cover=coverage)