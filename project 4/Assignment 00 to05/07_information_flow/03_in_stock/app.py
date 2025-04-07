inventory = {
    'pear': 1000,
    'apple': 500,
    'banana': 200,
    'orange': 0,
    'grape': 0
}

def num_in_stock(fruit):
    """Returns the number of the given fruit in stock."""
    return inventory.get(fruit.lower(), 0)  # Use lower() to handle case insensitivity

def main():
    # Prompt the user to enter a fruit
    fruit = input("Enter a fruit: ").strip().lower()  # Handle case insensitivity
    
    # Get the number of that fruit in stock
    stock = num_in_stock(fruit)
    
    # Check if the fruit is in stock and print appropriate message
    if stock > 0:
        print("This fruit is in stock! Here is how many:")
        print(stock)
    else:
        print("This fruit is not in stock.")

if __name__ == '__main__':
    main()
