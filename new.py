def get_valid_age():
    while True:
        try:
            age_input = input("Enter your age (0-120): ")
            age = int(age_input)
  
            else:
                print("Error: Age must be between 0 and 120.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer for age.")

valid_age = get_valid_age()
print(f"You entered a valid age: {valid_age}")
