import random

# -----------------------------
# Words and their hints
# -----------------------------
word_data = {
    "apple": "A popular fruit",
    "tiger": "A wild animal",
    "house": "A place where people live",
    "python": "A programming language",
    "school": "A place to study"
}

# Hangman stages
hangman = [
"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
"""
]

wins = 0
losses = 0

print("=" * 50)
print("🎮        WELCOME TO HANGMAN GAME")
print("=" * 50)

while True:

    word = random.choice(list(word_data.keys()))
    hint = word_data[word]

    guessed_letters = []
    attempts = 6

    print("\nNew Game Started!")
    print("Hint:", hint)

    while attempts > 0:

        print(hangman[6 - attempts])

        display = ""

        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "

        print("Word :", display)
        print("Guessed Letters :", " ".join(guessed_letters))
        print("Attempts Left :", attempts)

        if "_" not in display:
            print("\n🎉 Congratulations!")
            print("You guessed the word:", word)
            wins += 1
            break

        guess = input("\nEnter one letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter only ONE alphabet letter.")
            continue

        if guess in guessed_letters:
            print("⚠ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct!")
        else:
            attempts -= 1
            print("❌ Wrong!")

    if attempts == 0:
        print(hangman[6])
        print("\n💀 Game Over!")
        print("The correct word was:", word)
        losses += 1

    print("\n==============================")
    print("Scoreboard")
    print("==============================")
    print("Wins   :", wins)
    print("Losses :", losses)

    play = input("\nDo you want to play again? (yes/no): ").lower()

    if play != "yes":
        print("\nThanks for playing!")
        print("Final Score")
        print("Wins :", wins)
        print("Losses :", losses)
        break