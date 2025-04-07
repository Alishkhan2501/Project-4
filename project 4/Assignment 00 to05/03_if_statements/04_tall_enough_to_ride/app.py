
MINIMUM_HEIGHT : int = 50  # minimum height required for the ride

def main():
    height = float(input("How tall are you? "))  # Ask the user for their height and convert the input to a float
    if height >= MINIMUM_HEIGHT:  # Check if the user's height is greater than or equal to the minimum required height
        print("You're tall enough to ride!")  # Print this message if the user meets the height requirement
    else:
        print("You're not tall enough to ride, but maybe next year!")  # Print this message if the user is shorter than the required height

if __name__ == '__main__':
    main()
 