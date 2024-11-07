#Basic Calculator
import replit
import function
from art import logo

print(logo)

#recursive function for taking inputs
def calculator():
  num1 = float(input("Enter the number:\n"))
  for symbol in function.operations:
    print(symbol)

  to_continue = True

  #if there are more than 2 inputs
  while to_continue:
    operation = input("Pick an operation:\n")

    num2 = float(input("What is the next number:\n"))

    result = function.operations[operation](num1, num2)

    print(f"{num1} {operation} {num2} = {result}")

    #should continue the current opeartion or start a new operation
    continue_choice = input(
        "Pick 'y' to continue with other operation or 'n' to start a new calculation: "
    )

    replit.clear()

    if continue_choice == "y":
      to_continue = True
      num1 = result
    elif continue_choice == "n":
      to_continue = False
      calculator()
    else:
      print("Invalid choice")


#calling the calculator function
calculator()
