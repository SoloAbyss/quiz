import random

number = random.randint(1, 100)

print("I have chosen a random number between 1 and 100.")
print("Try to guess the number I have chosen!")
    
guesses = 0
    
while True:
    guess = int(input("Guess the number: "))

    guesses += 1

    if guess < number:
        print("It's a bigger number!")
            
    elif guess > number:
        print("It's a smaller number!")
            
    elif guess == number:
        print("You got it! Only took you " + str(guesses) + " guess(es)!")
        break
    else:
        print("Hmm that dosent seem right")

        

