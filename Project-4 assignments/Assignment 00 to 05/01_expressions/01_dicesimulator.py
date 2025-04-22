# Problem Statement
# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.
print ("07_tiny_mad_lib /n")
SENTENCE: str = "Panaversity is fun. I learned to program and used Python to make my "

def main():
    # Get the three inputs from the user 
    adjective: str = input("Please type an adjective and press enter. ")
    noun: str = input("Please type a noun and press enter. ")
    verb: str = input("Please type a verb and press enter. ")

    # Join the inputs together with the sentence starter
    print(SENTENCE + adjective + " " + noun + " " + verb + "!")

if __name__ == '__main__':
    main()


