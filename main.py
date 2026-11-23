
restaurant_list = []


def add_restaurant(restaurant_list):
    num_res = int(input("How many restaurants? "))

    for i in range(num_res):
        rname = input("Enter restaurant name: ")
        restaurant_list.append(rname)

    print("Restaurants added successfully!")


def view_restaurant(restaurant_list):
    if len(restaurant_list) == 0:
        print("No restaurants available")
    else:
        print("\n========== RESTAURANT LIST ==========")

        for i in range(len(restaurant_list)):
            print(i + 1, restaurant_list[i])


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


def total_restaurants(restaurant_list):
    print("Total restaurants:", len(restaurant_list))


# Main menu
while True:

    print("\n========== FOOD ORDERING SYSTEM ==========")
    print("1. Add Restaurant")
    print("2. View Restaurants")
    print("3. Search Restaurant")
    print("4. Remove Restaurant")
    print("5. Total Restaurants")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

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
        print("Thank you for using Food Ordering System!")
        break

    else:
        print("Invalid choice! Please try again.")
