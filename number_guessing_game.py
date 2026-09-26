import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0

print("🎯 Number Guessing Game")
print("I have selected a number between 1 and 100.")
print("Try to guess it!")

while True:
    try:
        guess = int(input("\nEnter your guess: "))
        attempts += 1

        if guess == secret_number:
            print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
            break

        elif guess < secret_number:
            print("❌ Too low!")

        else:
            print("❌ Too high!")

        # Hints decrease as attempts increase
        if attempts <= 2:
            difference = abs(secret_number - guess)

            if difference <= 5:
                print("💡 Hint: You are very close!")
            elif difference <= 15:
                print("💡 Hint: You are close.")
            else:
                print("💡 Hint: You are far away.")

        elif attempts <= 4:
            # Less specific hint
            if secret_number % 2 == 0:
                print("💡 Hint: The number is even.")
            else:
                print("💡 Hint: The number is odd.")

        elif attempts <= 6:
            # Very small hint
            if secret_number > 50:
                print("💡 Hint: The number is greater than 50.")
            else:
                print("💡 Hint: The number is 50 or less.")

        else:
            print("⚠️ No more hints! Keep trying.")

    except ValueError:
        print("Please enter a valid number.")