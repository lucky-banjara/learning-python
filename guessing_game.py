import random

easy_words = ["cat", "dogg", "house", "trees", "carpet"]
medium_words = ["python", "guitar", "mountain", "ocean", "computer"]
hard_words = ["encyclopedia", "philosophy", "architecture", "psychology", "astronomy"]

print("Welcome to the Password Guessing Game!\n")
print("Choose a difficulty level: easy, medium, hard\n")

level= input("Enter difficulty level\n").lower()

if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid dicciculty level. Defaulting to easy.")
    secret = random.choice(easy_words)

attempts= 0

print("Guess the secret Password")

while True:
    guess = input("Enter your guess:").lower()
    attempts += 1
    if guess == secret:
     print(f"Congratulations! You've guesses the password '{secret}' in {attempts} attempts!")
     break

    hint = " "

    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"
    print(f"Hint: {hint}")

    print("Game Over!")