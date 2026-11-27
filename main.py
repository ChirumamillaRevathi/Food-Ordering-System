
restaurant_list = []
food_menu = {}


# 1. Add Restaurant
def add_restaurant(restaurant_list):
    try:
        num_res = int(input("How many restaurants? "))

        if num_res <= 0:
            print("Please enter a number greater than zero")
            return

        for i in range(num_res):
            rname = input("Enter restaurant name: ")
            restaurant_list.append(rname)

        print("Restaurants added successfully!")

    except ValueError:
        print("Invalid input! Please enter numbers only.")


# 2. View Restaurants
def view_restaurant(restaurant_list):
    if len(restaurant_list) == 0:
        print("No restaurants available")
    else:
        print("\n========== RESTAURANT LIST ==========")

        for i in range(len(restaurant_list)):
            print(i + 1, restaurant_list[i])


# 3. Search Restaurant
def search_restaurant(restaurant_list):
    search_name = input("Enter restaurant name to search: ")

    found = False

    for name in restaurant_list:
        if name.lower() == search_name.lower():
            found = True
            break

    if found:
        print("Restaurant is listed")
    else:
        print("Restaurant is not listed")


# 4. Remove Restaurant
def remove_restaurant(restaurant_list):
    remove_name = input("Enter restaurant name to remove: ")

    found = False

    for name in restaurant_list:
        if name.lower() == remove_name.lower():
            restaurant_list.remove(name)
            found = True
            print("Restaurant removed successfully!")
            break

    if not found:
        print("Restaurant not found!")


# 5. Total Restaurants
def total_restaurants(restaurant_list):
    print("Total restaurants:", len(restaurant_list))


# 6. Add Food Items with Prices
def add_food_price(food_menu):
    try:
        num_food = int(input("How many food items do you want to add? "))

        if num_food <= 0:
            print("Please enter a number greater than zero.")
            return

        for i in range(num_food):
            food_name = input("Enter food name: ")
            price = float(input("Enter food price: "))

            if price < 0:
                print("Price cannot be negative. Please enter again.")
                price = float(input("Enter food price: "))

            food_menu[food_name] = price

        print("Food items added successfully!")

    except ValueError:
        print("Invalid input! Please enter a valid number.")


# 7. View Food Items and Prices
def view_food_price(food_menu):
    if len(food_menu) == 0:
        print("No food items available.")
    else:
        print("\n========== FOOD MENU ==========")

        for food_name, price in food_menu.items():
            print(food_name, "- ₹", price)


# 8. Search Food Item
def search_food(food_menu):
    search_name = input("Enter food name to search: ")

    found = False

    for food_name, price in food_menu.items():
        if food_name.lower() == search_name.lower():
            print("Food item:", food_name)
            print("Price: ₹", price)
            found = True
            break

    if not found:
        print("Food item not found!")

# 9. Remove Food Item
def remove_food(food_menu):
    remove_name = input("Enter food name to remove: ")

    found = False

    for food_name in food_menu:
        if food_name.lower() == remove_name.lower():
            del food_menu[food_name]
            found = True
            print("Food item removed successfully!")
            break

    if not found:
        print("Food item not found!")

# Update Food Price
def update_food_price(food_menu):
    food_name = input("Enter food name to update: ")

    found = False

    for name in food_menu:
        if name.lower() == food_name.lower():
            new_price = float(input("Enter new price: "))

            if new_price < 0:
                print("Price cannot be negative!")
                return

            food_menu[name] = new_price
            found = True

            print("Food price updated successfully!")
            break

    if not found:
        print("Food item not found!")


# Main Menu
while True:

    print("\n========== FOOD ORDERING SYSTEM ==========")
    print("1. Add Restaurant")
    print("2. View Restaurants")
    print("3. Search Restaurant")
    print("4. Remove Restaurant")
    print("5. Total Restaurants")
    print("6. Add Food Items")
    print("7. View Food Items")
    print("8. Search Food Item")
    print("10. Update Food Price")
    print("11. Exit")

    try:
        choice = int(input("Enter your choice: "))

    except ValueError:
        print("Invalid input! Please enter numbers only.")
        continue

    if choice == 1:
        add_restaurant(restaurant_list)

    elif choice == 2:
        view_restaurant(restaurant_list)

    elif choice == 3:
        search_restaurant(restaurant_list)

    elif choice == 4:
        remove_restaurant(restaurant_list)

    elif choice == 5:
        total_restaurants(restaurant_list)

    elif choice == 6:
        add_food_price(food_menu)

    elif choice == 7:
        view_food_price(food_menu)

    elif choice == 8:
        search_food(food_menu)

    elif choice == 9:
        remove_food(food_menu)

    elif choice == 10:
        update_food_price(food_menu)

    elif choice == 11:
        print("Thank you for using Food Ordering System!")
        break


    else:
        print("Invalid choice! Please try again.")
