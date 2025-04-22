print("02_pop_up_shop\n")
def fruits_products():
    fruits = {
        "apple": 10.0,
        "durian": 25.0,
        "jackfruit": 30.0,
        "kiwi": 15.0,
        "rambutan": 12.5,
        "mango": 8.0
    }
    total_cost = 0

    for fruit, price in fruits.items():
        quantity = int(input(f"How many {fruit} do you want?: "))
        total_cost += price * quantity

    print(f"Total cost: ${total_cost}")

if __name__ == "__main__":
    fruits_products()