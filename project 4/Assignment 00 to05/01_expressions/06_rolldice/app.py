import random  
NUM_SIDES = 6

def main():
    # Roll two dice
    die1 = random.randint(1, NUM_SIDES)  
    die2 = random.randint(1, NUM_SIDES)  
    sum = die1 + die2

    print(f"Dice have {NUM_SIDES} sides each.")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Sum of two dice: {sum}")

if __name__ == '__main__':
    main()
