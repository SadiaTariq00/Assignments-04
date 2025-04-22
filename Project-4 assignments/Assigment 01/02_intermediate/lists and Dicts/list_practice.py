# let's Practice some list methods

my_list = ["Mango", "Apple", "Banana" , "Orange", "Grapes", "Strawberry", "Kiwi", "Pineapple"]

def accessing_list_elements(my_list,index):
    """Returns the element at the specified index or an error message if out of range."""
    if 0 <= index < len(my_list):
        return f"Element at Index {index}: {my_list[index]}"
    return "Index out of range"
    
def modify_element(my_list,index,new_value):
    """Replaces the element at the specified index with a new value if index is valid."""
    if 0 <= index < len(my_list):
        old_value = my_list[index]
        my_list[index] = new_value
        return f"Replaced '{old_value}' with '{new_value}' at index {index}."
    return "Index out of range"

def slice_list(my_list,start,end):
    """Returns a sublist from start to end index, handling out-of-range cases."""
    if 0 <= start < len(my_list) and 0 <= end < len(my_list):
        return f'Sliced from list {my_list[start:end]}'
    return "Invalid slice range"

def list_game():
    print("\nWelcome to the List Game!")
    print("--------------------------")

my_list = ["Mango", "Apple", "Banana" , "Orange", "Grapes", "Strawberry", "Kiwi", "Pineapple"]
while True:
    print("\nCurrent List:", my_list)

    print("Choose an operation:")
    print("1. Access Element")
    print("2. Modify Element")
    print("3. Slice List")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':
        index = int(input("Enter index to access: "))
        print(accessing_list_elements(my_list, index))

    elif choice == '2':
        index = int(input("Enter index to modify: "))
        new_value = input("Enter new value: ")
        print(modify_element(my_list, index, new_value))

    elif choice == '3':
        start = int(input("Enter start index for slice: "))
        end = int(input("Enter end index for slice: "))
        print(slice_list(my_list, start, end))

    elif choice == '4':
        print("Exiting the game.")
        break

    else:
        print("Invalid choice! Please try again.")

if __name__ == "__main__":
    list_game()



   