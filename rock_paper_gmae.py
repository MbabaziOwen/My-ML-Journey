import random

options = ("rock","paper","scissors")
player = None
computer = random.choice(options)

while player not in options: 
    player = input("enter a choice ( rock , paper , scissors): ")

if player == "rock" and computer == "rock":
    print(f"its a draw , player picked {player},  and computer picked  {computer}")

elif player == "rock" and computer == "paper":
    print(f"computer wins , player picked {player},  and computer picked  {computer}")

elif player == "rock" and computer == "scissors":
    print(f"player wins , player picked {player},  and computer picked  {computer}")

elif player == "paper" and computer == "paper":
    print(f"Darw , player picked {player},  and computer picked  {computer}")

elif player == "paper" and computer == "rock":
    print(f"player wins , player picked {player},  and computer picked  {computer}")

elif player == "paper" and computer == "scissors":
    print(f"computer wins , player picked {player},  and computer picked  {computer}")

elif player == "scissors" and computer == "scissors":
    print(f"Draw , player picked {player},  and computer picked  {computer}")

elif player == "scissors" and computer == "paper":
    print(f"Play wins , player picked {player},  and computer picked  {computer}")

else:
    print(f"computer wins , player picked {player},  and computer picked  {computer}")




