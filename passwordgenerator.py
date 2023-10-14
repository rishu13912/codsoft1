import secrets
import string

def generate_password(length):
    # Define the character sets for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(secrets.choice(characters) for _ in range(length))

    return password

def main():
    try:
        # Prompt the user to specify the desired password length
        password_length = int(input("Enter the desired password length: "))

        if password_length <= 0:
            print("Password length should be a positive integer.")
            return

        # Generate the password
        password = generate_password(password_length)

        # Display the generated password
        print("Generated Password:", password)

    except ValueError:
        print("Invalid input. Please enter a valid positive integer for password length.")

if __name__ == "__main__":
    main()
