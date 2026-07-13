num=int(input("enter a number"))
if num<0:
    print("kindly use positive numbers")
elif num==0:
    print(f"Yes {num} is an armstrong number")
elif num>=0:
    temp=num
    arm=0
    count=0
    while(temp>0):
        temp=temp//10
        count+=1
    temp=num
    rem=0
    while(temp>0):
        rem=temp%10
        arm=arm+rem**count
        temp=temp//10
    if num==arm:
        print(f" given number {num} is an armstrong number")
    else:
        print(f"Given number {num} is not an armstrong number")


