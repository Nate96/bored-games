import random

ACTIVITIES = [
        "Take a Walk",
        "Organize Kitchen",
        "Take a walk",
        "Stretch for 10 minutes",
        "Declutter Work Space",
        "Learn a new word and use it in a sentence",
        "Watch your favorite movie",
        "5 minutes of Meditation",
        "Breathing Exercise",
        "Write a story for 5 minutes",
        "Go to a place the means a lot to you",
        "Play your favorite video game",
        "Read a chapter of a fiction book",
        "Text an old Friend",
        "Eat at a local Restaurants",
        "Clean for 10 minutes",
        ]

if __name__ == "__main__":
    random_index = random.randint(0, len(ACTIVITIES) - 1)
    print("Activity:", ACTIVITIES[random_index])
