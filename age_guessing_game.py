age = 22
guess = None 

while guess != age:
    try:
        guess = int(input("Enter the age: "))
        if guess < 18:
            print("Too low, That's Teenage age!")
        elif guess < age: 
            print("Wrong!, You guessed low.")    
        elif guess > age:
            print("Wrong, You guessed the age High. Try again! ")
    except ValueError:
        print("Please enter a valid age!")

print("Correct guessed!")
