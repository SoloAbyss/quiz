sentance = input("Enter a sentance: ")

if sentance == "":
    print("You didnt enter anything")
    length = input(int("Characters fro the left: "))
else:
    print("Great")



if length < 0:
    print("Thats to small!")

elif length > sentance:
    print("Thats too big!")

    