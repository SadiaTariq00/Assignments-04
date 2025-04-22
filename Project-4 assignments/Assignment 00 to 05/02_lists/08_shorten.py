print("08_shorten \n")

MAX_LENGTH:int = 3
def shorten(lst):
  while len(lst) >= MAX_LENGTH:
   last_element = lst.pop()   #pop method last elemnet remove krta h
   print(last_element)
def get_lst():
    lst = []
    elem: str = input("Please enter an element of the list. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list. ")
    return lst

def main():
      lst = get_lst()
      shorten(lst)

if __name__ == '__main__':
  main()