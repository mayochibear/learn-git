import random

def number_guessing_game():

    secret = random.randint(1, 100)
    guess = None
    lives = 3


    while guess != secret and lives != 0:
        try:
            guess = int(input("Guess the number: "))

            if guess < 1 or guess > 100:
                print("🚨 Please guess a number strictly between 1 - 100")
                lives -= 1
                continue

            if guess > secret:
                lives -= 1
                print("Too high!")
            elif guess < secret:
                lives -= 1
                print("Too low!")
            else:
                print("\n🎉 CONGRATULATIONS! 🎉")
                print(f"You guessed the number {secret} correctly!")
        except ValueError:
            print("❌ Invalid input. Please enter a whole number.")
            lives -= 1
            continue
    if lives == 0 and guess != secret:
        print("\n😔 GAME OVER!")
        print(f"You ran out of lives ({lives}).")
        print(f"The secret number was: {secret}.")
        print("Better luck next time!")
    

number_guessing_game()


