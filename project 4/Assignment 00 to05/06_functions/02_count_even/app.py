def count_even(lst):
    """Count and print the number of even numbers in the list."""
    even_count = sum(1 for number in lst if number % 2 == 0)
    print(f"The number of even numbers is: {even_count}")

def main():
    # Initialize an empty list to store the user input
    user_input = []
    
    # Keep prompting the user to enter integers until they press enter without input
    while True:
        user_value = input("Enter an integer or press enter to stop: ")
        
        # If the user presses enter without typing a number, stop the loop
        if user_value == "":
            break
        
        # Try to convert the input to an integer and append to the list
        try:
            user_input.append(int(user_value))
        except ValueError:
            print("That's not a valid integer, please try again.")
    
    # Call count_even to print the number of even numbers in the list
    count_even(user_input)

if __name__ == '__main__':
    main()
