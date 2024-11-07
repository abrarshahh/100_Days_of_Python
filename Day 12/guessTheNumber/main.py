import random
from art import logo

number_of_tries = 10
number = random.randint(1,100)

def play_game():
    global number
    global number_of_tries
    
    while number_of_tries:
            
        if number == user_number:
            print("Congrats You guessed correctly!!")
            
        else:
            print(f"You have {number_of_tries} tries remaining!!!")
            user_number = int(input("Guess the number: "))
            
            if number < user_number:
                print("You guessed a number that is too high!!!")
                number_of_tries-=1
            
            elif number > user_number:
                print("You guessed a number too low!!!")
                number_of_tries-=1
            
    if number_of_tries == 0:
        print(f"Better luck next time!! The number that i was thinking about is: {number}")

print(logo)
print("WELCOME TO THE NUMBER GUESSING GAME!")
print("I'm thinking of a number between '1' and '100'.")
level = input("Choose a difficulty. Type 'easy'or 'hard': ")

if level == "easy":
    play_game()

elif level == "hard":
    number_of_tries = 5
    play_game()