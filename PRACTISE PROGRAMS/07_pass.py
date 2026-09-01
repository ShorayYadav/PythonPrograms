# Take a password string and check basic rules (length ≥ 8 and contains at least one digit)
# Take a password string and check basic rules (length ≥ 8 and contains at least one digit)
password = input("Enter a password: ")
if len(password) >= 8:
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if has_digit:
        print("Valid password")
    else:
        print("Invalid password: must contain at least one digit")
else:
    print("Invalid password: must be at least 8 characters long")
