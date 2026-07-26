import random

print("====================================")
print("     WELCOME TO GUESS THE NUMBER")
print("====================================")

best_score = None

while True:

    # Generate random number
    secret_number = random.randint(1, 100)

    # Variables
    attempts = 0
    max_chances = 10
    guessed_numbers = []

    print("\nI have selected a number between 1 and 100.")
    print("You have 10 chances to guess it.")

    while attempts < max_chances:

        guess = int(input("\nEnter your guess: "))

        attempts += 1
        guessed_numbers.append(guess)

        if guess > secret_number:
            print("Too High! Try Again.")

        elif guess < secret_number:
            print("Too Low! Try Again.")

        else:
            print("\n🎉 Congratulations! You guessed the correct number.")
            print("You guessed it in", attempts, "attempt(s).")

            # Best Score
            if best_score is None or attempts < best_score:
                best_score = attempts

            break

        print("Remaining Chances:", max_chances - attempts)

    else:
        print("\n❌ Game Over!")
        print("The correct number was:", secret_number)

    # Display Guess Details
    if len(guessed_numbers) > 0:
        print("\n========== GAME SUMMARY ==========")
        print("All Guessed Numbers:", guessed_numbers)
        print("First Guess:", guessed_numbers[0])
        print("Last Guess:", guessed_numbers[-1])
        print("Total Number of Guesses:", len(guessed_numbers))

    if best_score is not None:
        print("Best Score:", best_score, "attempt(s)")

    # Play Again
    choice = input("\nDo you want to play again? (Yes/No): ").strip().lower()

    if choice != "yes":
        print("\nThank you for playing Guess the Number Game!")
        print("Goodbye!")
        break