def main():
    # Initialize an empty dictionary to store the count of each number
    number_count = {}

    while True:
        # Get user input and convert it to an integer
        user_input = input("Enter a number: ")
        
        # Check if the user entered an empty input (i.e., pressed enter without input)
        if user_input == "":
            break
        
        number = int(user_input)
        
        # Update the count of the number in the dictionary
        if number in number_count:
            number_count[number] += 1  # Increment count if the number is already in the dictionary
        else:
            number_count[number] = 1  # Add the number to the dictionary with an initial count of 1

    # Print the count of each number in the dictionary
    for number, count in number_count.items():
        print(f"{number} appears {count} times.")

# Ensure that the main function is called when the script is run directly
if __name__ == '__main__':
    main()
