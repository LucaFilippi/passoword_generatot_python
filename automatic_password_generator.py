# password_generator.py

import random
import string

def get_yes_or_no(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        print("Please enter 'y' or 'n'.")

def build_character_pool(use_upper, use_lower, use_digits, use_symbols):
    pool = ''
    if use_upper:
        pool += string.ascii_uppercase
    if use_lower:
        pool += string.ascii_lowercase
    if use_digits:
        pool += string.digits
    if use_symbols:
        pool += string.punctuation
    return pool

def generate_password(length, pool):
    return ''.join(random.choice(pool) for _ in range(length))

def main():
    print("=== Secure Password Generator ===\n")

    while True:
        try:
            length = int(input("Enter desired password length (8-64): "))
            if 8 <= length <= 64:
                break
            print("Length must be between 8 and 64.")
        except ValueError:
            print("Please enter a valid number.")


    use_upper = get_yes_or_no("Include uppercase letters? (y/n): ")
    use_lower = get_yes_or_no("Include lowercase letters? (y/n): ")
    use_digits = get_yes_or_no("Include numbers? (y/n): ")
    use_symbols = get_yes_or_no("Include symbols? (y/n): ")


    pool = build_character_pool(use_upper, use_lower, use_digits, use_symbols)

    if not pool:
        print("Error: At least one character type must be selected.")
        return


    password = generate_password(length, pool)
    print("\nYour generated password:", password)

if __name__ == "__main__":
    main()
