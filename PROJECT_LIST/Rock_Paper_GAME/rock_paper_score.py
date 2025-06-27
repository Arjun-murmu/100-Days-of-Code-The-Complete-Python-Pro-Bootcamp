from random import choice
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# print(rock)
# print(paper)
# print(scissors)
game_image = [rock, paper, scissors]
user_score = 0
computer_score = 0

def compare(u_choice, c_choice):
    global user_score, computer_score
    if u_choice == c_choice:
        print("Match is draw.")
    elif (u_choice == 0 and c_choice == 2) or (u_choice == 1 and c_choice == 0) or (u_choice == 2 and c_choice == 1):
        print("User Wins!")
        user_score += 1
    elif (c_choice == 0 and u_choice == 2) or (c_choice == 1 and u_choice == 0) or (c_choice == 2 and u_choice == 1):
        print("Computer Wins!")
        computer_score += 1
    else:
        print("You typed an invalid number. You lose.")
        computer_score += 1


def playgame():
    global user_score,computer_score
    is_game_over = False
    while not is_game_over:
        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
        if user_choice >= 0 and user_choice <= 2:
            print(game_image[user_choice])

        computer_choice = random.randint(0, 2)
        print(f"Computer chose {computer_choice}")
        print(game_image[computer_choice])

        compare(user_choice,computer_choice)

        should_game_c = input("Do you want to continue the game ? Type 'y' or 'n' : ").lower()
        if should_game_c == "n":
            is_game_over = True

    print(f"User score is {user_score}, computer score : {computer_score}")
    if user_score > computer_score:
        print("congratulations you Win😎.")
    elif user_score == computer_score:
        print("Score is equal. Match Draw😁.")
    else:
        print("You Lose.Computer win.😏.")

while input("You play this game ? Type 'y' or 'n':  ") == "y":
    print("\n" * 10)
    user_score = 0
    computer_score = 0
    playgame()
