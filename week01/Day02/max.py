count=int(input("How many numbers you want to add"))
a=int(input("enter the number"))
largest=second_largest=a
while(count>1):
    num=int(input("enter the number"))
    if num>largest:
        second_largest=largest
        largest=num
    elif num<largest and num>second_largest:
        second_largest=num
    elif num<largest and second_largest==largest:
        second_largest=num
    count-=1
if largest==second_largest: #duplicated numbers only
    print(f"Largest number is {a} and No second largest number exist")
else:
    print(f"Largest number is {largest} and second largest is {second_largest}")