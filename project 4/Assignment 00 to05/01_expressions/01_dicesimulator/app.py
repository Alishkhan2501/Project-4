import random
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total.
    """
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    dice_sum = die1 + die2  # Renaming 'sum' to 'dice_sum' to avoid conflict
    print("Sum of two dice:", dice_sum)

def main():
    die1 = 10  # Variable in main to demonstrate scope
    print(f"die1 in main() starts as: {die1}")
    roll_dice()
    roll_dice()
    roll_dice()
    print(f"die1 in main() is: {die1}")

if __name__ == '__main__':
    main()
