# Multiplication Table
def multiplication_table():
    try:
        x = int(input("Enter number: "))
        print(f"\nMultiplication Table of {x}")
        print("-------------------------")
        for i in range(1, 11):
            y = x * i
            print(f"{x} × {i} = {y}")
        print("Table end.")
    except ValueError:
        print("Please enter a valid number.")
# FizzBuzz
def fizzbuzz():
    print("\nFizzBuzz")
    print("--------")
    for i in range(1, 16):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
# Guessing Game
def guessing_game():
    secret_number = 7
    attempts = 0
    print("\nGuessing Game")
    print("-------------")
    while True:
        try:
            guess = int(input("Guess the number (1-10): "))
            attempts += 1
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")
def main():
    while True:
        print("\n===== Python Mini Projects =====")
        print("1. Multiplication Table")
        print("2. FizzBuzz")
        print("3. Guessing Game")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            multiplication_table()
        elif choice == "2":
            fizzbuzz()
        elif choice == "3":
            guessing_game()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Select 1-4.")
main()
