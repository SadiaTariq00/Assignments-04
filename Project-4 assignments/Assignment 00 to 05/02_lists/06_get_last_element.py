print("06_get_last_element \n")
def get_last_element(lst):
     print(lst[-1])     #last element chahiye iski [-1]

def get_lst():
    lst = []
    elem: str = input("Please enter an element of the list. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list. ")
    return lst

def main():
    lst = get_lst()
    get_last_element(lst)


if __name__ == '__main__':
      main()