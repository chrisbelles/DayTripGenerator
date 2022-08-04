# (5 points): As a developer, I want to make at least three commits with descriptive messages.

# (5 points): As a developer, I want to store my destinations, restaurants, mode of transportation, 
# and entertainment selections in their own separate lists.

# (5 points): As a user, I want a destination to be randomly selected for my day trip.

# (5 points): As a user, I want a restaurant to be randomly selected for my day trip.

# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.

# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.

# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, 
# mode of transportation, and/or form of entertainment if I don’t like one or more of those things.

# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like 
# all of the random selections.

# (10 points): As a user, I want to display my completed trip in the console.

# (5 points): As a developer, I want all of my functions to have a Single Responsibility. 
# Remember, each function should do just one thing!

import random

print("Welcome to The Day Trip Generator! It seems that you're ready for the cards to decide an adventure for you!")

destination = ["New York", "Rome", "San Diego", "Paris", "Brazil", "Naples", "Athens", "Mexico City", "Indianapolis", "Amsterdam"]

def destinationSelection():
    user_confirmation = False
    while user_confirmation is False:
        random_destination = random.choice(destination)
        print(f"The cards have selected {random_destination} for you.")
        user_input = input("Does this sound like a good time to you? y/n: ")
        if user_input == "y":
            print(f"It has been decided! {random_destination} will be the destination!! Let's decide how to get there!")
            return random_destination
        elif user_input == "n":
            print("That's okay, we shall shuffle the deck and try again.")


userApprovedDestination = destinationSelection()

restaurant = ["Biagi's", "Cheesecake Factory", "Island Prime", "Kokoro", "Morton's Steakhouse"]

transportation = ["Motorcycle", "Car", "Plane", "Train", "Bus"]

entertainment = ["See a play", "Museum", "Go-kart racing", "Local shopping", "Mini-golf"]

