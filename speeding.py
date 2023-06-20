
canine = "Dog"

feline = "Cat" 

animal_list = ["Dog", "Cat", "Kitten", "Dog", "Dog", "Cat", "Mr Semmons", "Cat", "Kitten", "Cat"]

animal_list.extend([input("Enter any animal: ")])

for animal in animal_list:
    if animal == canine:
        print("Woof")
    elif animal == feline:
        print("Meow")
    elif animal == "Kitten":
        print("Cute Meow")
    else:
        print("We dont recognize that")