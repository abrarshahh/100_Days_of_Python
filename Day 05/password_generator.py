#Password Generator
import random

d_letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

d_numbers = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

d_symbols = [
    '!', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=']

print("Welcome to PyPassword Generator!")

letter = int(input("How many letters would you like in your password: \n"))
symbols = int(input("How many symbols would you like in your password: \n"))
numbers = int(input("How many numbers would you like in your password: \n"))

passwordList = []

for i in range(letter):
  passwordList += random.choice(d_letters)

for j in range(symbols):
  passwordList += random.choice(d_symbols)
  
for k in range(numbers):
  passwordList += random.choice(d_numbers)

random.shuffle(passwordList)

password = ""
for p in passwordList:
  password += p

print(f"Here is a secure password for you:\n{password}")