print("00_guess_my_number \n")
import random
def main():
    secret_number = random.randint(1, 100)
    print ("I am thinking of a number between 1 and 100.")

    guess = int (input("Enter your guess: "))

    while guess != secret_number:
        if guess < secret_number:
            print ("Your guess is too low.")
        else:
            print ("Your guess is too high.")
        guess = int (input("Enter your guess: "))
    guess = int (input("Enter your guess: "))

    print("Congratulations! You guessed the number!") 
    
if __name__ == '__main__':
  main()    