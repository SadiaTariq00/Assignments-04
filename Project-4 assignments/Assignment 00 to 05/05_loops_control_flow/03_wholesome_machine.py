print("03_wholesome_machine\n")
correct_affirmation = ("I am capable of doing anything I put my mind to")

def main():
  print("Welcome the Wholesome machine")

  while True:
    user_input = input("Please type the following affirmation: ")
    
    # Check if input matches the affirmation
    if user_input == correct_affirmation:
        print("That's right! :)")
        break  
    else:
        print("Hmmm, that was not the affirmation. Try again.")

if __name__ == '__main__':
  main()