import random

number_to_guess =random.randint(1,100)
print("Welcome to the Guessing Game!\n")
print("I have selected a number between 1 and 100. Can you guess it?\n")
while True:
 try:
   guess = int(input("Enter your guess: "))
   if guess < number_to_guess:
      print("Too LOW! Try again.")
   elif guess > number_to_guess:
      print("Too High! Try again.")
   else:
      print("Congratulations! You guessed the number correctly!")
      break
 except ValueError:
   print("Please enter a valid integer.")


