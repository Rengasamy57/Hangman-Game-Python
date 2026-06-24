import random


words = ["python", "hangman", "computer", "internship", "developer"]


word = random.choice(words)

guessed_letters = []
attempts = 6

print("Welcome to Hangman!")
print("You have", attempts, "attempts to guess the word.")

while attempts > 0:
    
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print("\nWord:", display)

    print("Guessed letters:", ", ".join(guessed_letters) if guessed_letters else "None")

  
    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

  
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Good guess!")
    else:
        attempts -= 1
        print("Wrong guess!")

    print("Remaining attempts:", attempts)

if attempts == 0:
    print("\nGame Over! The word was:", word)