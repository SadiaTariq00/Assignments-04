print("02_e=mc2 \n")

C = 299792458

def main():

    mass = float(input("Enter kilos of mass: "))
    energy = mass * (C ** 2)

    # Output
    print("\ne = m * C^2...\n")
    print(f"m = {mass} kg \n")
    print(f"C = {C} m/s\n")
    print(f"{energy} joules of energy!")

# main function
if __name__ == "__main__":
    main()