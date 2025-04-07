def subtract_seven(num):
    """Subtracts 7 from the given number and returns the result."""
    num = num - 7
    return num

def main():
    # Set the initial value of num
    num = 7
    
    # Call subtract_seven() to subtract 7 from num
    num = subtract_seven(num)
    
    # Print the result (which should be zero after subtraction)
    print("This should be zero:", num)

if __name__ == '__main__':
    main()
