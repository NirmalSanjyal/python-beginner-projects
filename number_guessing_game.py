import random

number = random.randint(1, 10)
guess = None
tries = 0

while guess != number:
    try:
        guess = int(input("Guess a number between 1 and 10: "))
        tries += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
    except ValueError:
        print("Please enter a number!")

print(f"Correct! You guessed it in {tries} tries.")
