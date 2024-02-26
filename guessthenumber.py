from random import randint

n = randint(1, 100)


print("Guess a number in range 1 - 100")


def main():
    i = 0
    while True:
        try:
            i += 1
            x = int(input(f"Step {i}. Your number is: "))

            if x == n:
                print(f"Congrats, the number was {n}! You used only {i} steps!")
                break
            elif x > n:
                print("Too high. Try again.\n")
            else:
                print("Too small. Try again.\n")

            if i >= 5:
                print(f"Sorry, no more tries. The number was {n}")
                break
        except ValueError:
            print(f"Please, enter a number\n")


if __name__ == "__main__":
    main()
