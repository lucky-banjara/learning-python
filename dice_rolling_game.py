import random

while True:
    choice =input("Roll the dice! (y/n): ").lower()
    if choice == 'y':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1,6)
        print (f"You rolled: {dice1} and {dice2}")
    elif choice == 'n':
        print('Thanks for playing!')
        break
    else:
        print("Invalid input. Please enter 'y' or 'n' ")