import random

subjects = ["Sharukh Khan",
          "Salman Khan"
          "Amitabh Bachhan",
          "A Mumbai Cat",
          "A Group of Monkeys",
          "Prime Minister Balen",
          "Uber Driver"]

actions = ["launches",
           "cancels",
           "dances",
           "eats",
           "declares war on",
           "orders",
           "celebrates",]

places_or_things = ["at Perth",
                    "at Baldavis",
                    "during  World Cup",
                    "at Optus Stadium",
                    "in wedding",
                    "at a restaurant",
                    "at a party",
                    ]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"{subject} {action} {place_or_thing}"

    print("\n" + headline)
    user_input = input("\nDo you want another headline? (yes/no):").strip().lower()
    if user_input == "no":
        break

print("Thanks for using the Fake Headline Generator!")
    