a=int(input("Enter a number"))
if a<1:
    print("Number is invalid, please try with another number")
elif a==1:
    print(f"{a} is not a prime number")
else:
    for i in range(2,a):
        if a%i==0:
            break
    if i==a-1:
        print(f"{a} is a prime number")
    else:
        print(f"{a}is not a prime number")