#Fizz Buzz
number1 = int(input("Enter Starting Number: "))
number2 = int(input("Enter Ending Number: "))

for n in range(number1, number2+1):
  if n%3 == 0 and n%5 == 0:
    print("Fizz Buzz")
    
  elif n%3 == 0:
    print("Fizz")

  elif n%5 == 0:
    print("Buzz")

  else:
    print(n)