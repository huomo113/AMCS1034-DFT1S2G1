#import pyton libary 
import random

while True:
    #Generate a ranom value (1,2) to stimulate the coin flip
    answer = random.randint(1,2)

    #Prompt to enter the ser guess
    guess = int(input("Enter your guess as 1 for a head, 2 for a tail, or 0 to exit: "))

    if guess == 0:
        print("Thank you for playing the game!")
        break
    elif guess == 1 or guess == 2:
            if guess == answer:
                print("Your guess is correct!")
            else:
                print("Your guess is incorrect!")
    else:
            print("Please enter either 0, 1, or 2. \n")