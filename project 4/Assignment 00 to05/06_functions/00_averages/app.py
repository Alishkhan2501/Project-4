def main():
    # Prompt the user to enter the first number
    num1 = float(input("Enter the first number: "))
    # Prompt the user to enter the second number
    num2 = float(input("Enter the second number: "))

    # Compute the average of the two numbers
    average = (num1 + num2) / 2

    # Output the result
    print(f"The average of {num1} and {num2} is {average}.")

if __name__ == '__main__':
    main()
