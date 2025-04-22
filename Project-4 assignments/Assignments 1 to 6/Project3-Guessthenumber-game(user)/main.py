# Project: 02

import random  # Randomly generate a number

def guess_number():
    random_number = random.randint(1, 100) 
    attempts = 10  #
    
    print("Welcome! This is the Number Generator Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while attempts > 0:
        print(f"\nYou have {attempts} guesses left.")
        
        try:
            guess = int(input("Guess the number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if guess < random_number:
            print("Your guess is too low.")  
        elif guess > random_number:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! You guessed the correct number in {7 - attempts + 1} tries!")
            return
        
        attempts -= 1  # Reduce the number of attempts
    
    # If the user runs out of guesses
    print(f"\nYou ran out of guesses. The number was {random_number}.")

# Run the function
guess_number()