import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4")
        return ""

    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    special = string.punctuation

    # Ensure at least one character from each category
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(numbers),
        random.choice(special)
    ]

    # Fill the remaining length
    all_chars = lowercase + uppercase + numbers + special
    password += random.choices(all_chars, k=length - 4)

    # Shuffle to avoid predictable pattern
    random.shuffle(password)

    return "".join(password)


def main():
    print("=== Password Generator ===")
    try:
        length = int(input("Enter password length: "))
        password = generate_password(length)
        if password:
            print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()
