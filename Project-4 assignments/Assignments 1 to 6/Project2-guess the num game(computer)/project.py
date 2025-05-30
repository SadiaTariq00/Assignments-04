# Project: Guess the number game by computer.

import random
def guess_the_number():
    """ Project: Guess the number game by computer."""
    number = random.randint(1, 100)
    guesses_left = 7

    # Welcome message 
    print("Welcome to the number guessing game")
    print("I am thinking a number between 1 to 100")

    # Loop generated
    while guesses_left > 0:
        print(f"\nYou have {guesses_left} guesses left.")
        try:
            guess = int(input("Take a guess of another number: "))
        except ValueError:
            print("Invalid input: Please enter a number.")
            continue

        # Guess the secret number 
        if guess < number:
            print("Too low number. Try again!")
        elif guess > number:
            print("Too high number. Try again!")
        else:
            print(f"Congratulations! You got the correct number in {7 - guesses_left + 1} tries.")
            return
        
        guesses_left -= 1  # Reduce the guesses left
    
    # when all guesses are finished 
    print(f"\nYou ran out of guesses. The number was {number}.")

guess_the_number()