import random

def play_game():
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 10 attempts to guess it correctly.")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 10

    while attempts > 0:
        try:
            # Get the user's guess
            guess = int(input("Enter your guess: "))

            # Check if the guess is correct
            if guess == number_to_guess:
                print("Congratulations! You guessed the number correctly!")
                break
            elif guess < number_to_guess:
                print("Too low!")
            else:
                print("Too high!")

            # Reduce the number of attempts
            attempts -= 1
            print(f"Attempts remaining: {attempts}")
        except ValueError:
            print("Please enter a valid number.")

    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    play_game()
