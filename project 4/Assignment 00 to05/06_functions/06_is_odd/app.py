def main():
    # Loop through numbers 10 to 19
    for num in range(10, 20):
        # Check if the number is even or odd
        if num % 2 == 0:
            print(f"{num} even")
        else:
            print(f"{num} odd")

if __name__ == '__main__':
    main()
