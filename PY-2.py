import random
import string

def generate_password(length):
    """Generate a random secure password of a specified length."""
    if length < 6:
        print("Password length should be at least 6 characters for security.")
        return None
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_characters = lowercase + uppercase + digits + symbols
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    password += random.choices(all_characters, k=length - 4)

    random.shuffle(password)
    return ''.join(password)

try:
    length = int(input("Enter the desired password length (minimum 6): "))
    generated_password = generate_password(length)
    if generated_password:
        print("Generated Password:", generated_password)
except ValueError:
    print("Invalid input! Please enter a valid number.")








