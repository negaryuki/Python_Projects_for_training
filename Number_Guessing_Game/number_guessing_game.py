import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        user_guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if user_guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    number_guessing_game()
