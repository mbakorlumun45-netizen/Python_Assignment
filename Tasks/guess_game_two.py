import random

secret_number = random.randint(1, 1000)
run = True
print("Between 1 to 1000, guess a number: ")
guess = int(input("Enter your guess: "))

while run:

    if guess > secret_number:

        print("Too high. try again")
        guess = int(input("Enter your guess: "))

    elif guess < secret_number:
        print("Too low. try again")
        guess = int(input("Enter your guess: "))

    elif guess == secret_number:
        print("congratulations. you got it right")
        print("play again")
        guess = int(input("Enter your guess: ")) 
    else:
        guess = int(input("Enter your guess: ")) 
        

   




