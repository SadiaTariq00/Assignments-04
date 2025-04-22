print("04_pythagorean_theorem \n")
import math

def main():
  ab :float= float(input("Enter the length of side AB: "))
  ac :float = float(input("Enter the length of side AC: "))
  bc : float= math.sqrt(ab**2 + ac**2)

  # output
  print ("The length of side BC is: " + str(bc))

#main function
if __name__ == "__main__":
  main()