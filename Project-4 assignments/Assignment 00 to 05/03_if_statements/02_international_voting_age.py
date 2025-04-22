print("02_international_voting_age\n")

PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48
def main():
  all_ages = int(input("How old are you ? "))

  if all_ages >= PETURKSBOUIPO_AGE:
    print("You can vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")
  else:
      print("You cannot vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")

  if all_ages >= STANLAU_AGE:
    print("You can vote in Stanlau where the voting age is "+ str(STANLAU_AGE) + ".")
  else:
      print("You cannot vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")

  if all_ages >= MAYENGUA_AGE:
    print("You can vote in Mayengua where the voting age is "+ str(MAYENGUA_AGE) + ".")
  else:
      print("You cannot vote in Mayengua where the voting age is " + str(MAYENGUA_AGE) + ".")

if __name__ == "__main__":
  main()