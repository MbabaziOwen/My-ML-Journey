#python guessing game
import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num,highest_num)

guesses = 0

is_running = True

while is_running:
    guess = input("enter a guess for the random number")
    if guess == answer:
        print(f"you guessed the number it is, {answer}, and you guessed it on your ,{guesses}th try  ")
        break    
    else:
        print("try again ")
        continue

