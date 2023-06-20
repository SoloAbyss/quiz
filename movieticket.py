

what_movie = input("\n\nNow Showing:\nGuardians Of The Galaxy - Vol 3\nThe Super Mario Bros Movie\nJohn Wick: Chapter 4\n\nWhat movie do you wanna watch?\n")

age = int(input("Cool! How old are you?\n"))

if age < 12:
    print("Perferct, your ticket for " + what_movie + " will be $14.50")
elif age > 12 and age < 19:
    print("Cool, your ticket for " + what_movie + " will be $18.00")
elif age > 19 and age < 65:
    print("Cool, your ticket for " + what_movie + " will be $20.50")
elif age > 65:
    print("Great old cow, your ticket for " + what_movie + " will be $15.50")
else:
    print("welp")
