def greet(name):
    print(f"Greetings {name}!")

def main():
    # Get the user's name
    name = input("What's your name? ")
    
    # Call the greet function with the user's name
    greet(name)

if __name__ == '__main__':
    main()
