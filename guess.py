import random

print("🎮 Welcome to the Guessing Game!")
secret = random.randint(1, 100)

attempts = 0

while True:
    guess = input("Guess a number between 1 and 100: ")
    attempts += 1

    if not guess.isdigit():
        print("❌ Please enter a number.")
        continue

    guess = int(guess)

    if guess < secret:
        print("🔻 Too low!")
    elif guess > secret:
        print("🔺 Too high!")
    else:
        print(f"✅ Correct! You guessed it in {attempts} attempts.")
        break
