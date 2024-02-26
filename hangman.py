import random

def main():
    word = choose_word()
    guessed_letters = []
    tries = 6

    while True:
        print("\nAttempts left:", tries)
        print("Word:", display_word(word, guessed_letters))

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            print("Correct!")
        else:
            tries -= 1
            print("Incorrect!")

        if guess == word:
            print("\nCongratulations! The word is:", word)
            break
    
        if "_" not in display_word(word, guessed_letters):
            print("\nCongratulations! The word is:", word)
            break
        elif tries == 0:
            print("\nSorry, you can't try anymore. The word was:", word)
            break
        

def choose_word():
    word_list = ["step", "gita", "python", "hangman", "exam", "grade", "django", "semester", "family", "name", "country"]
    return random.choice(word_list)


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


main()