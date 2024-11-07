import random
from data import data
import art


# Generating a random integer from the length of the data to use as index    
item_a_index = random.randrange(len(data))
item_b_index = random.randrange(len(data))

# Fetching the data from the randomly generated index
item_a = data[item_a_index]
item_b = data[item_b_index]

# intializing cont variable to keep the program running until "False"
cont = True
# intializing score variable to keep the track of points
score = 0

# starting the loop
while cont:
    print("\n" * 20)
    print(art.logo)
    print(f"Compare A: {item_a['name']}, a {item_a['description']}, from the country of {item_a['country']}")
    print(art.vs)
    print(f"Against B: {item_b['name']}, a {item_b['description']}, from the country of {item_b['country']}")

    choice = input("Who has more followers? Type 'A' or 'B': ")

    if choice == 'A' or choice == 'a':
        ## checking if the users choice is correct
        if item_a['follower_count'] > item_b['follower_count']:
            print("Congrats!! You have got it right")
            
            ### changing the next question for B item
            item_b_index = random.randrange(len(data)) 
            item_b = data[item_b_index]
            
            ### storing the point gained 
            score += 1   
            
        else:
            print("You Lose!!!😭")
            print(f"Your Final Score is {score} points.")
            
            ### Breaking the loop when the player looses
            cont = False
            
    elif choice == 'B' or choice == 'b':
        ## checking if the users choice is correct
        if item_a['follower_count'] < item_b['follower_count']:
            print("Congrats!! You have got it right")
            
            ### changing the next question for item a and item b
            item_a = item_b
            item_b_index = random.randrange(len(data)) 
            item_b = data[item_b_index]  
            
            ### storing the point gained
            score += 1 
        else:
            print("You Lose!!!😭")
            print(f"Your Final Score is {score} points.")
            
            ### Breaking the loop when the player looses
            cont = False
            
            
    # For User Input Validation        
    else:
        print("Choose the Valid option!!")