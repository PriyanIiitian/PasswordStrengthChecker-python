import re
import getpass

def check_password_strength():
    password = getpass.getpass('Enter the password:')
    strength = 0
    remarks = ''
    lower_count=upper_count=num_count=wspace_count=special_count=0

def password_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1

    if re.search(r'[A-Z]', password):
        strength += 1

    if re.search(r'[a-z]', password):
        strength += 1

    if re.search(r'[@$!%*?&]', password):
        strength += 1

    if re.search(r'[0-9]', password):
        strength += 1

    if strength == 5:
        return "Strong"
    elif 3 <= strength < 5:
        return "Medium"
    else:
        return "Weak"

password = input("Enter a password: ")
print(f"The password strength is: {password_strength(password)}")
