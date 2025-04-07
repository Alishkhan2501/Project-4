def main():
    AFFIRMATION = "I am capable of doing anything I put my mind to."

    print("Please repeat the following affirmation exactly as it is:")
    print( AFFIRMATION)

    while True:
        user_input = input("> ")  # Get user input

        if user_input ==  AFFIRMATION:
            print("That's right! ")
            break
        else:
            print("\nOops! That was not the correct affirmation. Try again.")
            print("Please repeat the affirmation again:")
            print( AFFIRMATION)

# Run the main function
if __name__ == "__main__":
    main()
