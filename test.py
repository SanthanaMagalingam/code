import re

def get_valid_integer(prompt, min_val=None, max_val=None):
    """Prompts the user for an integer and validates it against optional min/max values."""
    while True:
        try:
            user_input = int(input(prompt))
            if min_val is not None and user_input < min_val:
                print(f"Error: Input must be at least {min_val}.")
            elif max_val is not None and user_input > max_val:
                print(f"Error: Input must be at most {max_val}.")
            else:
                return user_input
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")



# Example Usage:
if __name__ == "__main__":
    # Validate an integer within a range
    age = get_valid_integer("Enter your age (between 0 and 120): ", min_val=0, max_val=120)
    print(f"Your age is: {age}")

    # Validate a non-empty string
    name = get_non_empty_string("Enter your name: ")
    print(f"Your name is: {name}")

    # Validate an email address
    while True:
        email_input = input("Enter your email address: ")
        if validate_email(email_input):
            print(f"Your email is: {email_input}")
            break
