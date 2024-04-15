import random

fruits = ["apple", "banana", "orange", "grape", "mango", "watermelon", "apricot", "kiwi", "papaya", "lime", "lemon", "grapefruit", "fig", "plum", "nectarine", "coconut", "avocado", "guava", "dragonfruit", "starfruit"]
player_name = input("What is your name? ")

# Greet the player and introduce the fruit quiz
print("Welcome to the Fruit Quiz, " + player_name + "!")
print("Test your knowledge on delicious fruits!\n")

# To set up the quiz with 10 questions
num_questions = 10

# To keep track of score, attempts, and asked questions
score = 0
attempts = 0
asked_questions = []

for _ in range(num_questions):
    # Randomly select a fruit that hasn't been asked yet
    fruit = random.choice([f for f in fruits if f not in asked_questions])

    description = ""

    if fruit == "apple":
        description = "I'm red, round, and crunchy. I come in many varieties."
    elif fruit == "banana":
        description = "I'm yellow, curved, and full of potassium. Monkeys love me!"
    elif fruit == "orange":
        description = "I'm orange, juicy, and rich in vitamin C. I'm great for breakfast!"
    elif fruit == "grape":
        description = "I'm small, purple, and grow in clusters. Wine is made from me!"
    elif fruit == "mango":
        description = "I'm tropical, yellow, and have a sweet, juicy flesh. I'm often used in smoothies!"
    elif fruit == "watermelon":
        description = "I'm big, green, and juicy. I'm great for a refreshing summer treat!"
    elif fruit == "apricot":
        description = "I'm orange, fuzzy, and have a sweet pit. I'm often dried or used in jams!"
    elif fruit == "kiwi":
        description = "I'm fuzzy, green, and have a black center. I'm sour and sweet, and high in vitamin C!"
    elif fruit == "papaya":
        description = "I'm orange, melon-like, and have black seeds. I'm good for digestion!"
    elif fruit == "lime":
        description = "I'm small, green, and have a sour taste. I'm often used in drinks and guacamole."
    elif fruit == "lemon":
        description = "I'm similar to a lime, but yellow and even more sour. I'm great in lemonade and desserts."
    elif fruit == "grapefruit":
        description = "I'm larger than an orange and have a pink or yellow flesh. I can be sweet, tart, or bitter."
    elif fruit == "fig":
        description = "I'm small, purple, and have a unique flavor. I'm often dried or used in jams."
    elif fruit == "plum":
        description = "I'm small, round, and have a smooth skin. My color varies from purple to red to yellow, and I'm sweet and juicy."
    elif fruit == "nectarine":
        description = "I'm similar to a peach, but smooth-skinned and slightly more tart."
    elif fruit == "coconut":
        description = "I'm brown and hairy on the outside, with a sweet, white flesh and refreshing water inside."
    elif fruit == "avocado":
        description = "I'm green, pear-shaped, and have a creamy, buttery texture. I'm often used in guacamole."
    elif fruit == "guava":
        description = "I'm small, green or yellow, and have sweet or tart flesh with many seeds."
    elif fruit == "dragonfruit":
        description = "I'm unique with pink or red skin and white or black flesh. My taste is slightly sweet and floral."
    elif fruit == "starfruit":
        description = "I'm yellow when ripe and shaped like a star. My taste is a mix of sweet, tart, and sour."

    # Get the players guess (and convert it to lowercase for comparison)
    guess = input(f"What fruit am I? ({description})\n").lower()

    # Check if the guess is correct
    attempts += 1
    if guess == fruit:
        score += 1
        print("Correct! You guessed the right fruit.\n")
    else:
        print(f"Oh no, that's not it. I was thinking of {fruit.title()}s.\n")  # .title is to capitalize for display

    # Add the answered fruit to the list of asked questions so it doesn't ask the same question
    asked_questions.append(fruit)

# Show the final results
print(f"Your final score is {score} out of {num_questions}.")
print(f"You attempted to guess {attempts} times.")

# Congratulate the player based on their score
if score == num_questions:
    print("Wow, you got them all right! You're a fruit expert, " + player_name + "!")
elif score > num_questions // 5:
    print("Great job, " + player_name + "! You know your fruits well.")
else:
    print("Don't worry, keep practicing and you'll be a fruit master in no time!")

# To allow the player to review their answers and choose when to exit
input("\nPress Enter to Exit")
