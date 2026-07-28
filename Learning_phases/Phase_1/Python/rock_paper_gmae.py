import random

options = ("rock","paper","scissors")
player = None
computer = random.choice(options)

is_running = True

while is_running:
    player = None
    computer = random.choice(options)


    while player not in options or player != "q": 
        player = input("enter a choice ( rock , paper , scissors): ")
        computer = random.choice(options) 

    if player == "rock" and computer == "rock":
        print(f"its a draw , player picked {player},  and computer picked  {computer}")
        computer = random.choice(options) 

    elif player == "rock" and computer == "paper":
        print(f"computer wins , player picked {player},  and computer picked  {computer}")
        computer = random.choice(options) 

    elif player == "rock" and computer == "scissors":
        print(f"player wins , player picked {player},  and computer picked  {computer}")
        computer = random.choice(options) 

    elif player == "paper" and computer == "paper":
        print(f"Darw , player picked {player},  and computer picked  {computer}")
        computer = random.choice(options) 

    elif player == "paper" and computer == "rock":
        print(f"player wins , player picked {player},  and computer picked  {computer}")
        computer = random.choice(options) 

    elif player == "paper" and computer == "scissors":
        print(f"computer wins , player picked {player},  and computer picked  {computer}")
        computer = random.choice(options) 

    elif player == "scissors" and computer == "scissors":
        print(f"Draw , player picked {player},  and computer picked  {computer}")
        computer = random.choice(options) 

    elif player == "scissors" and computer == "paper":
        print(f"Play wins , player picked {player},  and computer picked  {computer}")
        computer = random.choice(options) 

    elif player == "scissors" and computer == "rock":
        print(f"computer wins , player picked {player},  and computer picked  {computer}")
        computer = random.choice(options) 
    elif player == "q" :
        is_running = False
        print("you have ended the game")





