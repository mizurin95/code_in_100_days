import random
import os

def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

deck = [2,3,4,5,6,7,8,9,10,10,10,10,11]

def shuffle_cards(cards):
    card = random.choice(cards)
    return card

def calculate_cards(cards):
    """Calculate sum of cards on hand""" 
    #Return 0 when BlackJack(Ace + 10) - hand with only 2 cards   
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    # When sum over 21 and have ace in hand, 11 becomes 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_score(dealer_score, player_score):
    if dealer_score == player_score:
        return "Draw"
    elif dealer_score == 0:
        return "You lose, Oppenent won with BlackJack"
    elif player_score == 0:
        return "You win with BlackJack"
    elif dealer_score > 21:
        return "You win, oppenent went over 21"
    elif player_score > 21:
        return "You went over 21, Lose"
    elif dealer_score > player_score:
        return "You lose"
    else:
        return "You win"
            
def game_play():
    dealer_cards = []
    player_cards = []    

    #Add 2 cards to dealer and player
    for i in range(2):
        dealer_cards.append(shuffle_cards(deck))
        player_cards.append(shuffle_cards(deck))

    dealer_score = calculate_cards(dealer_cards)
    player_score = calculate_cards(player_cards)

    print(f"Dealer's first cards: {dealer_cards}, dealer's score: {dealer_score}")
    print(f"Player's cards:{player_cards}, player's score:{player_score}")
    
    if player_score < 21:
        if input("Do you want to draw another card? Type 'y' or 'n': ") == 'y':
            player_cards.append(shuffle_cards(deck))
            player_score = calculate_cards(player_cards)
            print(f"Player's cards: {player_cards}, player's score: {player_score}")
        else:
            print(compare(dealer_score, player_score))
    else:
        print(compare(dealer_score, player_score))
    while dealer_score < 17:
        dealer_cards.append(shuffle_cards(deck))
        dealer_score = calculate_cards(dealer_cards)

game_play()




