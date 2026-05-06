import random

print(" Welcome to the Number Guessing Game!")

while True:

    print("\nSelect Difficulty Level:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-200)")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        limit = 50
        max_attempts = 5

    elif choice == '2':
        limit = 100
        max_attempts = 7

    elif choice == '3':
        limit = 200
        max_attempts = 10

    else:
        print(" Invalid Choice")
        continue

    secret_number = random.randint(1, limit)

    print(f"\nI have selected a number between 1 and {limit}")
    print(f"You have {max_attempts} attempts!")

    attempts = 0

    while attempts < max_attempts:

        guess = int(input("\nEnter your guess: "))
        attempts += 1

        if guess < secret_number:
            print(" Too Low!")

        elif guess > secret_number:
            print(" Too High!")

        else:
            print(f"\n Congratulations! You guessed the number in {attempts} attempts.")
            break

    else:
        print(f"\n Game Over! The correct number was {secret_number}")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != 'yes':
        print(" Thanks for playing!")
        break