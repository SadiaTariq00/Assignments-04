print("03_leap_year\n")

def main():
    # User se input lena
    year = int(input('Please input a year: '))

    # Pehla check: 4 se divide hota hai?
    if year % 4 == 0:
        # Dusra check: 100 se divide hota hai?
        if year % 100 == 0:
            # Teesra check: 400 se bhi divide hota hai?
            if year % 400 == 0:
                print("That's a leap year!")  # Har 3 condition true — leap year
            else:
                print("That's not a leap year.")  # 100 se divide hota hai, lekin 400 se nahi — not a leap year
        else:
            print("That's a leap year!")  # 4 se divide hota hai, lekin 100 se nahi — leap year
    else:
        print("That's not a leap year.")  # 4 se bhi divide nahi hota — not a leap year

if __name__ == '__main__':
  main()
