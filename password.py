
import re

def check_password(password):

    # Check whether password is empty
    if password == "":
        print("Password cannot be empty.")
        return

    # Check whether password contains spaces
    if " " in password:
        print("Password must not contain spaces.")
        return

    score = 0
    suggestions = []

    # Rule 1: Minimum length of 8 characters
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    # Rule 2: At least one uppercase letter
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter")

    # Rule 3: At least one lowercase letter
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter")

    # Rule 4: At least one digit
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add a digit")

    # Rule 5: At least one special character
    if re.search(r"[^A-Za-z0-9\s]", password):
        score += 1
    else:
        suggestions.append("Add a special character")

    # Display password strength
    print("\n----- PASSWORD STRENGTH REPORT -----")

    if score <= 2:
        print("Strength: Weak ({}/5)".format(score))

    elif score <= 4:
        print("Strength: Medium ({}/5)".format(score))

    else:
        print("Strength: Strong ({}/5)".format(score))

    # Display suggestions
    if suggestions:
        print("\nSuggestions:")
        for suggestion in suggestions:
            print("-", suggestion)
    else:
        print("No suggestions. Your password is secure.")

    print("------------------------------------")


# Main Program
print("====================================")
print("       PASSWORD STRENGTH CHECKER")
print("====================================")

password = input("Enter your password: ")

check_password(password)
