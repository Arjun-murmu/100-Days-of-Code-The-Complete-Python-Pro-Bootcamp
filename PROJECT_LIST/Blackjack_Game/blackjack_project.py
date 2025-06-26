import random
from random import choice

import art


# print(art.logo)

#STEP 4
def deal_card():
    """Return a random card form deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
# print(deal_card())


def calculate_score(cards):
    # if 11 in cards and 10 in cards and len(cards) == 2:
    """Take a list of cards and return score calculated from the cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

#STEP 5
def play_game():
    print(art.logo)
    user_card = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False


    for _ in range (2):
        new_card = deal_card()
        user_card.append(new_card)

        computer_cards.append(deal_card())

    # print(user_card)
    # print(computer_cards)
    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_cards)
        print(f"Your card : {user_card}, Current score : {user_score}")
        print(f"Computer card : {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            choice_play = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if choice_play == "y":
                user_card.append(deal_card())
            else:
                is_game_over = True

    #Hits 12
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand : {user_card}, final score : {user_score}")
    print(f"Computer's final hand : {computer_cards}, Final score : {computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n':  ") == "y":
    print("\n" * 20)
    play_game()

# def calculate_score():
#     # cardss = [3,5,6]
#     # return sum(cardss)
#     user_score = sum(user_card)
#     return user_score

# print(calculate_score())
