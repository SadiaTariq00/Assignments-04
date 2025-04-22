print("05_get_first_element \n")
def get_first_element(lst):
     print(lst[0])

def get_lst():
    lst = []
    elem: str = input("Please enter an element of the list. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list. ")
    return lst

def main():
    lst = get_lst()
    get_first_element(lst)


if __name__ == '__main__':
      main()