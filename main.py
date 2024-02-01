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
start_again = True
rps = [rock, paper, scissors]
choices = ["Rock", "Paper", "Scissors"]
player_choice = 0
print("Let's Play Rock Paper and Scissors!")
while start_again:

    game_start = True

    while game_start:

        player_choice = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors: "))

        if player_choice not in range(0, 3):
            print("Only choose 0 for rock, 1 for paper, and 2 for scissors.")
        else:
            game_start = False

    computer_choice = random.randint(0, 2)

    print(f"You chose:{choices[player_choice]} {rps[player_choice]}")
    print("VS \n")
    print(f"Computer chose:{choices[computer_choice]} {rps[computer_choice]}")

    if (player_choice == 2 and computer_choice == 1) or (player_choice == 0 and computer_choice == 2) or (
            player_choice == 1 and computer_choice == 0):
        print("You win")
    else:
        print("You lost")

    if input("Do you want to play again?: ").lower() == "no":
        print("Thank you for playing!")
        start_again = False
    else:
        print("\n")
