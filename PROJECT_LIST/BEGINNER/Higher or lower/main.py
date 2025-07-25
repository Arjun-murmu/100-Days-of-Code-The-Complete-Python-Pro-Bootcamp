#Display art
from xml.sax.handler import all_features

from art import logo,vs,end
from game_data import data
import random

def fromat_name(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f" {account_name}, a {account_description}, from {account_country}."

def check(user_guess,a_followers,b_followers):
    if a_followers > b_followers:
        return user_guess == 'a'
    else:
        return user_guess == 'b'

print(logo)
score = 0
game_should_continue = True

# Generate a random account from the game data
account_b = random.choice(data)

#make the game repeatable
while game_should_continue:
    # Making account at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {fromat_name(account_a)}")
    print(vs)
    print(f"Against B : {fromat_name(account_b)}")

    # - Get follower count of each account
    a_followers = account_a['follower_count']
    b_followers = account_b['follower_count']
    print(a_followers, b_followers)
    # Ask user for a guess.
    user_guess = input("Who was more follows? Type 'A' or 'B' : ").lower()

    # # Clear the screen
    # print("\n" * 20)
    # print(logo)

    # # - Get follower count of each account
    # a_followers = account_a['follower_count']
    # b_followers = account_b['follower_count']

    # Check if user is correct.
    is_correct = check(user_guess,a_followers,b_followers)

    # Give user feedback on their guess.
    #Score keeping

    if is_correct:
        score += 1
        print(f"You're right! Current score: : {score}.")
        # Clear the screen
        print("\n" * 20)
        print(logo)

    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False
        print(end)

