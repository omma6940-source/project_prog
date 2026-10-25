
password=(input("enter apassword"))

has_upper=False
has_lower=False
has_number=False
long_password=len(password)>=8

for letter in password:
    if letter.isupper():
        has_upper=True
    if letter.islower():
        has_lower=True
    if letter.isdigit():
        has_number=True

if has_upper and has_lower and has_number and long_password:
    print("your password is strong:")

else:
    print("your password is week:")
    if not has_upper:
        print("at least one uppercase")
    if not long_password:
        print("enter password 8 character")
    if not has_lower:
        print("at least one lowercase")
    if not has_number:
        print("enter least one number")