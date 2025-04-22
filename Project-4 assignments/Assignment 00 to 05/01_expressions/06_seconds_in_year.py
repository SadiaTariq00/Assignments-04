print("06_seconds_in_year \n")

DAYS_IN_A_YEAR: int = 365
HOURS_IN_A_DAY: int = 24
MIN_IN_A_HOUR: int = 60
SEC_IN_A_MIN: int = 60

def main():
    print("There are " + str(DAYS_IN_A_YEAR * HOURS_IN_A_DAY * MIN_IN_A_HOUR * SEC_IN_A_MIN) + " seconds in a year!")

# main function
if __name__ == '__main__':
    main()