from art import logo

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]


#caesar function for encryption and decryption
def caesar(plain_text, shift_amount, shift_direction):
  caesar_text = ""
  if shift_direction == "decode":
    shift_amount *= -1
  for char in plain_text:

    #different actions if text is alphabet only or mixture of symbols and numbers
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      caesar_text += alphabet[new_position]

    else:
      caesar_text += char

  print(f"The {shift_direction}d text is '{caesar_text}'.")


#printing the logo
print(logo)

should_continue = True

while should_continue:

  #inputs
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  #changing shift value in case of a larger number
  shift = shift % 26

  #calling the function
  caesar(plain_text=text, shift_amount=shift, shift_direction=direction)

  answer = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

  if answer == "no":
    should_continue = False
    print("Goodbye!")
