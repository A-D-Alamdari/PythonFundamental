"""
Rock wins against Scissors.
Scissors win against paper.
Paper wins against rock.

This is simple code with using random library and if-else statement for playing
Rock, Scissors, Paper game against computer.
"""

import random as r

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

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.  "))

if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)
else:
    print("Invalid Input!!")

computer_choice = r.randint(0, 2)

print("Computer chose:")
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)

if (choice == 0 and computer_choice == 2) \
        or (choice == 2 and computer_choice == 1) \
        or (choice == 1 and computer_choice == 0):
    print("You Win :)")
else:
    print("You Lose :(")

