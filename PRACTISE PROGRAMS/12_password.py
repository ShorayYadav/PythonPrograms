#10. Take a password string and check basic rules (length ≥ 8 and contains at least one digit)
Pass = input("Enter your password: ")

hasDigit = False
for char in Pass:
    if char.isdigit():
        hasDigit = True

if len(Pass) >= 8 and hasDigit:
    print("Your Password is Valid")
else:
    print("Re-enter your password")
    print("(make sure your password must follow basic rules: length >= 8 and contains at least one digit)")