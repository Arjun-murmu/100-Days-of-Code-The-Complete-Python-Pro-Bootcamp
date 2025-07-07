import random
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

# Function to set difficult
def set_difficult(game_type):
    if game_type == "easy":
        # print("You have 10 attempts remaining to guess the number.")
        # easy_game()
        return EASY_LEVEL
    elif game_type == "hard":
        # print("You have 5 attempts remaining to guess the number.")
        # hard_game()
        return HARD_LEVEL
    else:
        print("Invalid Type.")

def check_ans(user_guess,actual_number):
    """Check the answer against check, return the number of turns remaining."""
    if user_guess < actual_number:
        print("Too low!")
    elif user_guess > actual_number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number {actual_number}!")
        # break # Exit the loop if correct

def check_answer(user_guess,actual_number,turn):
    if user_guess < actual_number:
        print("Too low!")
        return turn - 1
    elif user_guess > actual_number:
        print("Too high!")
        return turn - 1
    else:
        print(f"Congratulations! You guessed the number {actual_number}!")
        # break # Exit the loop if correct
def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    game_type = input("Choose a difficulty. Type 'easy' or 'hard : ").lower()
    # Choosing the random number 1 to 100
    secret_number = random.randint(1,100)
    # print(secret_number)
    turn = set_difficult(game_type)
    guess = 0

    while guess != secret_number:
        print(f"You have {turn} attempts remaining to guess the number.")
        guess = int(input("Make Guess : "))
        # Track the number of turn and reduce the number of 1 if the number is wrong
        turn = check_answer(guess,secret_number,turn)
        if turn == 0:
            print("You've run out of guesses.you lose.")
            return
        elif guess != secret_number:
            print("Guess again")


play_game()

# while input("Do you want to play this game ? Type 'y' or 'n':  ") == "y":
#     print("\n" * 20)
#     play_game()










