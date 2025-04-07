
PETURKSBOUIPO_AGE: int = 16
STANLAU_AGE: int = 25
MAYENGUA_AGE: int = 48

def main():

    age = int(input("How old are you? "))  # Convert the input into an integer
    
    # Check voting eligibility in Peturksbouipo
    if age >= PETURKSBOUIPO_AGE:
        print(f"You can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")
    else:
        print(f"You cannot vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")
    
    # Check voting eligibility in Stanlau
    if age >= STANLAU_AGE:
        print(f"You can vote in Stanlau where the voting age is {STANLAU_AGE}.")
    else:
        print(f"You cannot vote in Stanlau where the voting age is {STANLAU_AGE}.")
    
    # Check voting eligibility in Mayengua
    if age >= MAYENGUA_AGE:
        print(f"You can vote in Mayengua where the voting age is {MAYENGUA_AGE}.")
    else:
        print(f"You cannot vote in Mayengua where the voting age is {MAYENGUA_AGE}.")

if __name__ == '__main__':
    main()
