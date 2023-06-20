menu = {
    "mince & cheese pie": 3.20,
    "mince and cheese pie": 3.20,
    "steak & cheese pie": 3.20,
    "steak and cheese pie": 3.20,
    "sausage roll": 5.20,
    "mince pie": 3.20,
    "filled roll": 5.60,
    "fanta": 4.50,
    "coke": 4.50,
    "sprite": 4.50
}

cart = {}

# Displays the Menu

def disp_menu():
    print("The Menu:\n")
    for item, price in menu.items():
        print(f"{item.capitalize()}: ${price:.2f}")

def buy_item(item, quantity):
    item = item.lower()
    if item not in menu:
        print("Sorry, we don't sell that here.")
    elif quantity < 0:
        print("You can't do that!")
    else:
        if item in cart:
            cart[item] += quantity
        else:
            cart[item] = quantity
        print(f"Cool, added {quantity} {item}(s) to your cart!")


def remove_item(item, quantity):
    if item in cart:
        if quantity >= cart[item]:
            del cart[item]
        else:
            cart[item] -= quantity
        print(f"Removed {quantity} {item}(s) from your cart.")
    else:
        print("That item is not inside your cart.")

def display_cart():
    total_cost = 0
    print("Items in your cart:")
    for item, quantity in cart.items():
        price = menu[item]
        item_cost = price * quantity
        total_cost += item_cost
        print(f"{item.capitalize()}: {quantity} x ${price:.2f} = ${item_cost:.2f}")
    print(f"Total cost: ${total_cost:.2f}")

while True:
    print("\nWelcome to Bussin Bakery")
    print("1. Whats on the menu?")
    print("2. Add item to your cart")
    print("3. Remove an item from your cart")
    print("4. Display your cart")
    print("5. Exit")

    choice = input("Enter your choice from above(1-5): ")

    if choice == '1':
        disp_menu()
    elif choice == '2':
        item = input("Enter the item you want to add: ").lower()
        quantity = int(input("How many do you want?: "))
        buy_item(item, quantity)
    elif choice == '3':
        item = input("Enter the item you want to remove: ").lower()
        quantity = int(input("How many do you want to remove: "))
        remove_item(item, quantity)
    elif choice == '4':
        display_cart()
    elif choice == '5':
        print("Thank you for shopping with Bussin Bakery!")
        break
    else:
        print("Hmm. That doesn't look right | Please try again.")


    


