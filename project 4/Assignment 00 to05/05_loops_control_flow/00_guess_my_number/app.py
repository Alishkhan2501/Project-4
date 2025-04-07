import random

def main():
    # Generate a random secret number between 0 and 99
    number_to_guess = random.randint(1, 99)
    
    print("I am thinking of a number between 0 and 99...")
    
    # Prompt the user for their first guess
    guess = int(input("Enter a guess: "))

    while guess != number_to_guess:  # Loop until the guess matches the secret number
         # Check if the guess is too low
        if guess < number_to_guess:         
            print("Your guess is too low.")
        # Check if the guess is too high
        else:
            print("Your guess is too high.")
            print()  # Print an empty line to separate guesses for better readability
        # Prompt the user to enter a new guess
        guess = int(input("Enter a new guess: "))  
    
    # Congratulate the user once they guess the correct number
    print(f"Congrats! The number was: {number_to_guess}")

if __name__ == '__main__':
    main()
