def validate_password(password):
    valid = True
    if len(password) < 6 or len(password) > 10:
        print(f'Password must be between 6 and 10 characters')
        valid = False
    if not password.isalnum():
        print(f"Password must consist only of letters and digits")
        valid = False
    digit = 0
    for character in password:
        if character.isdigit():
            digit += 1
    if digit < 2:
        print(f'Password must have at least 2 digits')
        valid = False
    return valid


password_entry = input()
check_validity = validate_password(password_entry)
if check_validity:
    print('Password is valid')
