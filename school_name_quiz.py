import random

schools = ["Namuna", "Everest", "Trinity", "Kathmandu", "KIST"]
answer = random.choice(schools)
guess = ""
chances = 3

print("🎓 Guess the School Name")
print(f"(Hint: Choose from: {', '.join(schools)})")
print("You have 3 chances!\n")

while guess.lower() != answer.lower() and chances > 0:
    guess = input("Enter your guess: ")

    if guess.lower() == answer.lower():
        print("🎉 Correct! You guessed the right school!")
        break
    else:
        chances -= 1
        if chances > 0:
            print(f"❌ Wrong! Try again. Chances left: {chances}\n")
        else:
            print(f"💀 Out of chances! The correct answer was: {answer}")

