print("07_get_list\n")

def main():
  lst = []

  val = input("Enter a value to add the list: ")
  while val:
    lst.append(val)
    val = input ("Enter a value to add the list: ")
  print("Here is the list: ", lst)

if __name__ == '__main__':
  main()