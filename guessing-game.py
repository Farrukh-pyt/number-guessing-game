import random

number = random.randint(1, 100)
attempts = 0
guess = None

print("Guess a number between 1 and 100")

while guess != number:
    try:
        guess = int(input("Your guess: "))
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break
    except ValueError:
        print("Please enter a valid number")
