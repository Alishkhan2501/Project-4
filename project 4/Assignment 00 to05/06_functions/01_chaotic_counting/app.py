
import random

DONE_LIKELIHOOD = 0.3   # 30% chance that we stop counting early

def done():
    """Simulate a random check for whether to stop counting."""
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    """Count from 1 to 10, stopping early if done() returns True."""
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    for i in range(1, 11):
        if done():
            return  # Stop counting and exit the function early
        print(i, end=" ")

def main():
    chaotic_counting()
    print("I'm done.")

if __name__ == '__main__':
    main()

