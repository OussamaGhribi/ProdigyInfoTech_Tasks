import re

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Add special characters (e.g., !, @, #, etc.).")

    if strength == 5:
        rating = "Strong 💪"
    elif 3 <= strength < 5:
        rating = "Moderate ⚠️"
    else:
        rating = "Weak ❌"

    return rating, feedback

if __name__ == "__main__":
    user_password = input("Enter your password: ")
    rating, suggestions = check_password_strength(user_password)

    print(f"\nPassword Strength: {rating}")
    if suggestions:
        print("Suggestions to improve:")
        for tip in suggestions:
            print(f"- {tip}")
