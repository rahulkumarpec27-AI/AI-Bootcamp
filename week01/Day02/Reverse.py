num=(input("enter a number"))
num=int(num)
rev=0
if (num<0):
    print("Please enter positive numbers")
else:
    while (num>0):
        div=num%10
        rev=rev*10+div
        num=num//10
    print(f"Reveral of number is {rev}")