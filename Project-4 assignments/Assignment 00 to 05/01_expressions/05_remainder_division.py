print("05_remainder_division \n")

def main():
  num1 = int(input("Please enter an integer to be divided: "))
  num2 = int(input("Please enter an integer to divide by: "))

  quotient = num1 // num2 # divide
  remainder = num1 % num2 # remainder

   # print the statement
  print(f"The result is divided by  {quotient} with a remainder of {remainder}.")

# run function
if __name__ == "__main__":
  main()