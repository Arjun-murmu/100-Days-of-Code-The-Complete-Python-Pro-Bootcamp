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
game_image = [rock,paper,scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 0 and user_choice <= 2:
    print(game_image[user_choice])

computer_choice = random.randint(0,2)
print(f"Computer chose {computer_choice}")
print(game_image[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print("User Wins!")
elif computer_choice == 0 and user_choice == 2:
    print("You Loss.")
elif computer_choice > user_choice:
    print("Computer Wins!")
elif computer_choice == user_choice:
    print("Match is draw.")
else:
    print("You Type an invalid number. You loss.")
