import random

# Ask user how many rounds they want to play
rounds = 8
score = 0

def main():
# Welcome message
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

# Loop for each round
for round_num in range(1, rounds + 1):
    print(f"\nRound {round_num}")
    
    # Generate numbers
    your_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)
    
    # Show user number
    print(f"Your number is {your_number}")
    
    # Ask for guess
    guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
    
    # Determine actual comparison
    if your_number > computer_number:
        actual = "higher"
    elif your_number < computer_number:
        actual = "lower"
    else:
        actual = "equal"
    
    # Check result and update score
    if guess == actual:
        print(f"You were right! The computer's number was {computer_number}")
        score += 1
    elif actual == "equal":
        print(f"Aww, that's incorrect. The computer's number was {computer_number}")
    else:
        print(f"Aww, that's incorrect. The computer's number was {computer_number}")
    
    print(f"Your score is now {score}")

# End of game message
print("\nThanks for playing!")

if __name__ == '__main__':
    main()
