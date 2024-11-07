# Hangman Game

import random

from replit import clear

import hangman_word
import hanmanart

# List of words for game
#word_list = ["python", "Mouse", "keyboard"]

chosen_word = random.choice(hangman_word.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

# Creating blanks
display = []
for _ in range(word_length):
  display += "_"

print(hanmanart.logo)

# User guessing
while not end_of_game:
  guess = input("Guess an alphabet of the word: \n").lower()

  clear()

  if guess in display:
    print("You already guessed that!")

  #Check guessed letter
  for position in range(word_length):
    letter = chosen_word[position]

    if letter == guess:
      display[position] = letter

  #join all elemnts of the list and then print it
  print(f"{' '.join(display)}")

  #check for lives
  if guess not in chosen_word:
    lives -= 1
    print(f"{guess} is a not present in the word!")
    print(f"You have {lives} lives left.")
    if lives == 0:
      end_of_game = True
      print("You lost!")

  elif guess in chosen_word:
    print("You guessed correctly!")
    print(f"You have {lives} left.")

  #check if user got all letters
  if "_" not in display:
    end_of_game = True
    print("You Win!")

  #print images of hangman
  print(hanmanart.stages[lives])
