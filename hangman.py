import random


class Hangman:
    def __init__(self, words):
        self.words = words
        self.secret_word = random.choice(self.words)
        self.guesses = []
        self.max_attempts = 10
        self.attempts_left = self.max_attempts

    def display_word(self):
        displayed_word = ""
        for letter in self.secret_word:
            if letter in self.guesses:
                displayed_word += letter
            else:
                displayed_word += "_"
        return displayed_word

    def guess_letter(self, letter):
        self.guesses.append(letter)
        if letter not in self.secret_word:
            self.attempts_left -= 1

    def guess_word(self, word):
        if word.lower() == self.secret_word:
            self.guesses.extend(word.lower())
        else:
            self.attempts_left -= 1

    def is_game_over(self):
        if self.attempts_left <= 0:
            return True, "\nSorry, you can't try anymore. The word was: " + self.secret_word
        elif '_' not in self.display_word():
            return True, "\nCongratulations! The word is: " + self.secret_word
        return False, ""


def main():
    words = ["step", "gita", "python", "hangman", "exam", "grade",
             "django", "semester", "family", "name", "country"]
    game = Hangman(words)

    print("Guess the word:", game.display_word())

    while not game.is_game_over()[0]:
        guess = input("\nGuess a letter: ").lower()
        if len(guess) == 1:
            game.guess_letter(guess)
        else:
            game.guess_word(guess)
        print("\nWord:", game.display_word())
        print("Attempts left:", game.attempts_left)

    print(game.is_game_over()[1])


if __name__ == "__main__":
    main()
