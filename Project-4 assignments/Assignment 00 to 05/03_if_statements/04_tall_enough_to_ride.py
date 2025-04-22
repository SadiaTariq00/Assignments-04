print("04_tall_enough_to_ride\n")

MINIMUM_HEIGHT : int = 50

def main():
  your_height= float(input("How tall are you? "))
  if your_height >= MINIMUM_HEIGHT:
    print("You're tall enough to ride!")
  else:
      print("You're not tall enough to ride, but maybe next year!")

if __name__ == '__main__':
  main()
