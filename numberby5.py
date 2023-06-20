number_list = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

number_list.extend([int(input("Type in a number: "))])

for number in number_list:
    if number % 5:
        print("You can times this by five!")
    else:
        print("You cant times this by five")

