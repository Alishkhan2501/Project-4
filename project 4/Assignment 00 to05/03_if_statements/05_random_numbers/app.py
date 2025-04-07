import random  # Import the random module to generate random numbers

N_NUMBERS = 10  # Total number of random numbers 
MIN_VALUE = 1  # Minimum value for the random number range
MAX_VALUE = 100  # Maximum value for the random number range

def main():
    #using loop to generate 10 random numbers
    for _ in range(N_NUMBERS):  # Repeat 10 times
        print(random.randint(MIN_VALUE, MAX_VALUE))  # Generate and print a random number between 1 and 100

if __name__ == '__main__':
    main()
