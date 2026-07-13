password=input("Enter your password")
count=0
while True:
    if len(password)<=8:
        print("Password is less than 8 characters")
        count=count-1
    a=any(char.isupper() for char in password)
    if a==False:
        print("It does not contain uppercase letter")
        count=count-1
    a=any( char.islower() for char in password)
    if a==False:
        print("It does not contain lowercase letter")
        count=count-1
    a=any(char.isdigit() for char in password)
    if a==False:
        print("It does not contain digits")
        count=count-1
    a=any( not char.isalnum() for char in password)
    if a==False:
        print("it does not contain special character")
        count=count-1
    break
if count==0:
    print("Strong Password")

