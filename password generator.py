import random
import string

def generate_password(length, complexity):
    if complexity == "low":
        chars = string.ascii_letters + string.digits
    elif complexity == "medium":
        chars = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "high":
        chars = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase
    else:
        print("Invalid complexity level. Please choose from 'low', 'medium', or 'high'.")
        return None

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator App")
    length = int(input("Enter the desired length of the password: "))
    complexity = input("Enter the complexity level (low, medium, high): ")

    password = generate_password(length, complexity.lower())
    if password:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
