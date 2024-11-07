import random
from art import logo

def deal_cards():
    '''Returns a random card from the deck'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    '''This Function takes the list of cards and returns the sum/score from those cards'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare_cards(player_score, computer_score):
    '''Compares the score of user with computer to decide a winner'''
    if player_score == computer_score:
        return "Draw :)"
    elif computer_score == 0:
        return "You Lose!!!, opponent has blackjack"
    elif player_score == 0:
        return "You win with a Blackjack"
    elif player_score > 21:
        return "You went over! \nBetter Luck Next Time!!"
    elif computer_score > 21:
        return "Opponent went over! \nYou Win!!"
    elif player_score > computer_score:
        return "You Win!!!"
    else:
        return "You Lose!!!"

def play_game():
    '''This function starts the game'''
    
    print(logo)
    
    player_cards = []
    computer_cards = []
    player_score = -1
    computer_score = -1
    is_game_over = False

    for i in range(2):
        player_cards.append(deal_cards())
        computer_cards.append(deal_cards())
        
    print(f"You Cards: {player_cards}")
    print(f"Computer card: {computer_cards[0]}")

    while not is_game_over:   
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            player_should_deal = input("Type 'y' to get another card or 'n' to pass: ")
            if player_should_deal == 'y':
                player_cards.append(deal_cards())

            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)


    print(f"Your Final hand is: {player_cards} and Final score is: {player_score}")
    print(f"Computer's Final hand is: {computer_cards} and Final score is: {computer_score}")
    print(compare_cards(player_score,computer_score))
    
while input("Do you wanna play a game of BlackJack? Type 'Y' or 'n': ") == 'y':
    print("\n"*20)
    play_game()