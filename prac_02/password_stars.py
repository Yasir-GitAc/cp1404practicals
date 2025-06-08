MIN_LENGTH = 8  # minimum password length

password = input("Enter your password: ")

while len(password) < MIN_LENGTH:
    print(f"Password too short! It must be at least {MIN_LENGTH} characters.")
    password = input("Enter your password: ")

print("*" * len(password))
