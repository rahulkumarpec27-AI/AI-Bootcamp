count=int(input("How many numbers you want to add"))
largest=second_largest=0
while(count>0):
    num=int(input("enter the number"))
    if num>largest:
        second_largest=largest
        largest=num
    elif num<largest and num>second_largest:
        second_largest=num
    count-=1
print(f"Largest number is {largest} and second largest is {second_largest}")