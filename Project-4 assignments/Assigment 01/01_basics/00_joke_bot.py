
PROMPT = "What do you want? "
JOKE = "Here is a joke for you! Why don't programmers need glasses? Because they can C#."
SORRY = "Sorry I only tell jokes"


def main():
    user_input = input(PROMPT)
    # Conditional response
    if user_input == "Joke":
        print(JOKE)
    else:
        print(SORRY)

if __name__ == "__main__":
    main()        
