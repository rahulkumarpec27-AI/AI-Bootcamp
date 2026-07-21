def reverse(l):
    temp=len(l)-1
    for i in range(0,(len(l)//2)):
        l[i],l[temp]=l[temp],l[i]
        temp-=1
    return (l)
    
def frequency(l):
    dict1={}
    for i in l:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1
    print(f"Count of duplicate is {dict1}")

def duplicate(l):
    dict1={}
    for i in l:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1
    l1=[]
    for i in dict1:
        if dict1[i]>1:
            l1.append(i)
    if len(l1)>0:
        print(f"Duplicate letters are {l1}")
    else:
        print("No duplicate element found")

l=list(input("enter list"))
print(reverse(l))