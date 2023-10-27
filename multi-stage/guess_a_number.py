import random

def main():
    while True:
        random_digit = random.randint(0, 9)

        user_input = input("Please enter a number (0 to 9) or 'q' to quit: ")

        if user_input.lower() == "q":
            break

        try:
            user_input = int(user_input)
            if 0 <= user_input <= 9:
                if user_input == random_digit:
                    print("Congratulations! You guessed the correct number.")
                else:
                    print(f"Sorry, the correct number was {random_digit}. Try again!")
            else:
                print("Oops, the number is not within the range (0 to 9).")
        except ValueError:
            print("Oops, it doesn't look like a valid integer.")

    print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    main()