def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    return low <= n <= high

def main():
    # Test the function with some examples
    print(in_range(5, 1, 10))  # Expected: True
    print(in_range(15, 1, 10))  # Expected: False
    print(in_range(1, 1, 10))   # Expected: True
    print(in_range(10, 1, 10))  # Expected: True
    print(in_range(0, 1, 10))   # Expected: False

if __name__ == '__main__':
    main()
