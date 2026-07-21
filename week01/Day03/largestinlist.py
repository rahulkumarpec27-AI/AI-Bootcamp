l=list(map(int, input("Enter numbers: ").split()))
max1=max2=max3=l[0]
for i in l:
    if i>max1:
        max3,max2,max1=max2,max1,i
    elif max1>i>max2 or max2==l[0]:
            max3,max2=max2,i
    elif max2>i:
        if max3==l[0] or max3<i:
            max3=i
if max1==max2==max3:
    print(f"first largest number in list is {max1} and no second largest and third largest number exists")
elif max2==max3 :
    print(f"first largest number is {max1}, second largest number is {max2} and no third largest number exists")
else:
    print(f"largest number is {max1}, second largest number is {max2} and third largest number is {max3}")


