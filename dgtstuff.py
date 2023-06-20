number = int(input("Enter a number between 1 and 12: "))

if number < 1 or number > 12:
    print("Invalid input. Please enter a number between 1 and 12.")
    
else:
    print("Times tables for {}: ".format(number))
    for i in range(1, 13):
        product = number * i
        print("{} x {} = {}".format(i, number, product))



