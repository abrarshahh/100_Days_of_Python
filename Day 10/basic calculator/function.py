#functions of calculator
#addition
def add(num1,num2):
  return num1+num2

#subtraction
def subtract(num1,num2):
  return num1-num2

#multiplication
def multiply(num1,num2):
  return num1*num2

#divison
def divide(num1,num2):
  return num1/num2


operations = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide,
}