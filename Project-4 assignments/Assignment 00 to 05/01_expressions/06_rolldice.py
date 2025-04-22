import random
# This program simulates rolling two dice.
TOTAL_SIDES: int = 6

def main():
    die1: int = random.randint(1, TOTAL_SIDES)
    die2: int = random.randint(1, TOTAL_SIDES)

    # Get their total
    total: int = die1 + die2

    # Print out the results
    print("Dice have", TOTAL_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)
# call the main() function.
if __name__ == '__main__':
    main()