import re

print(" PASSWORD STRENGTH CHECKER ")

while True:

    password = input("\nEnter your password: ")

    strength = 0

    # Length Check
    if len(password) >= 8:
        strength += 1
    else:
        print(" Password should contain at least 8 characters")

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        print(" Add at least one uppercase letter")

    # Lowercase Check
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        print(" Add at least one lowercase letter")

    # Number Check
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        print(" Add at least one number")

    # Special Character Check
    if re.search(r"[!@#$%^&*()_+=<>?/]", password):
        strength += 1
    else:
        print(" Add at least one special character")

    # Final Result
    if strength == 5:
        print(" Strong Password ")

    elif strength >= 3:
        print(" Medium Password")

    else:
        print(" Weak Password")

    again = input("\nDo you want to check another password? (yes/no): ").lower()

    if again != "yes":
        print(" Exiting Password Checker")
        break