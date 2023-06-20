gamingpc_dict = {"CPU": "Core i9 13900KS",
                 "GPU": "RTX 4090",
                 "RAM": "64GB"}


while True:

    what_part = input("Ask what parts are in the pc or type 'exit' to quit:. For e.g. CPU:\n")

    if what_part == "CPU":
        print(gamingpc_dict["CPU"])

    elif what_part == "GPU":
        print(gamingpc_dict["GPU"])

    elif what_part == "RAM":
        print(gamingpc_dict["RAM"])

    elif what_part == "exit":
        break

    else:
        print("Thats not a valid part!")
       