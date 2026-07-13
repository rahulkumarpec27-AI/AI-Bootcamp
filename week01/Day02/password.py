password=input("Enter your password")
a=True
while True:
    if len(password)<=8:
        a=False
        print("Password is less than 8 characters")
    a=any(char.isupper() for char in password)
    if a==False:
        print("It does not contain uppercase letter")
    a=any( char.islower() for char in password)
    if a==False:
        print("It does not contain lowercase letter")
    a=any(char.isdigit() for char in password)
    if a==False:
        print("It does not contain digits")
    a=any( not char.isalnum() for char in password)
    if a==False:
        print("it does not contain special character")
    break
if a==True:
    print("Strong Password")