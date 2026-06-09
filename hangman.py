import random

words = {
    "python": "Programming Language",
    "apple": "Fruit",
    "tiger": "Animal",
    "india": "Country",
    "laptop": "Electronic Device",
    "place" : "Srinagar",
    "patato" : "Vegetable",
    "tabla" : "Instrumemt"
    }

score = 0

while True:
    word, hint = random.choice(list(words.items()))
    guessed = ["_"] * len(word)
    attempts = 8

    print("\n🎮 Welcome to Hangman Game")
    print("Hint:", hint)

    while attempts > 0 and "_" in guessed:
        print("\nWord:", " ".join(guessed))
        print("Attempts Left:", attempts)

        letter = input("Enter a letter: ").lower()

        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    guessed[i] = letter
            print(" Correct Guess")
        else:
            attempts -= 1
            print(" Wrong Guess")

    if "_" not in guessed:
        print("\n You Won!")
        print("Word was:", word)
        score += 10
    else:
        print("\n You Lost!")
        print("Word was:", word)

    print(" Score:", score)

    choice = input("\nPlay Again? (yes/no): ").lower()
    if choice != "yes":
        break
    