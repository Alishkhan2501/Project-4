from hashlib import sha256

def hash_password(password):
    """Hashes the given password using the SHA256 algorithm."""
    return sha256(password.encode()).hexdigest()

def login(email, stored_logins, password_to_check):
    """
    Verifies if the hash of the entered password matches the stored hash
    for the provided email. Returns True if they match, otherwise False.
    """
    return stored_logins.get(email) == hash_password(password_to_check)

def main():
    """
    Simulates a basic login system where users provide their email
    and password. The system checks if the provided password matches the
    stored hash in a secure manner.
    """
    stored_logins = {
        "jane.doe@fighter.com": "e99a18c428cb38d5f260853678922e03",  # Hashed password for jane.doe
        "alice@bob.com": "e9bb1c23f7a82a2e9f768fe0b1a0faab",  # Hashed password for alice@bob
        "alix@marvel.com": "5e884898da28047151d0e56f8dc6292773603d0d810a63e6fd9c41e93d9e1d26"  # Hashed password for alix@marvel
    }
    
    # Request user to input their email and password (Removed extra space at the beginning)
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    # Check if the login is successful by comparing the hashed password
    if login(email, stored_logins, password):
        print("Login successful! Welcome!")
    else:
        print("Login failed. Invalid email or password. Please try again.")

if __name__ == '__main__':
    main()
