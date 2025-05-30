# Problem Statement
# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

# Here's a sample run of the program (user input is in bold italics):
# What is the length of side 1? 3
# What is the length of side 2? 4
# What is the length of side 3? 5.5
# The perimeter of the triangle is 12.5

def main():
    side1 : float = float(input("What is the length of side 1? "))
    side2 : float = float(input("What is the length of side 2? "))
    side3 : float = float(input("What is the length of side 3? "))

    # calling the perimeter
    perimeter : float= float(side1 + side2 + side3)

    # print the all sides of traingle
    print(f'The perimeter of the triangle is {perimeter}')

    #calling main function
if __name__ == "__main__":
    main()    