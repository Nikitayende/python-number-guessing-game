
import random

number = random.randint(1, 10)

guess = 0

while guess != number:

    guess = int(input("Enter Your Guess (1-10): "))

    if guess == number:
        print("🎉 Correct Guess!")

    elif guess > number:
        print("Too High")

    else:
        print("Too Low")

print("The Secret Number was:", number)
