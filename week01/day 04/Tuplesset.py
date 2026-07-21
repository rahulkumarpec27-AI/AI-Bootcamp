#Remove duplicate from list
'''L=list(map(int , input("enter the list").split()))
s=[]
for i in L:
    if i not in s:
        s.append(i)
del L
print(f"Unique list become {s}")
'''
#Rotate List
L=list(map(int,input("Enter list").split()))
k=int(input("Enter the right rotation count"))
s=k%len(L)
'''#L1=L[len(L)-s:]
#L2=L[0:(len(L)-s)]
L[len(L)-s:].extend(L[0:(len(L)-s)])
print(f"The rotated list is {L}")
'''
'''for i in range(0,s):
    for i in range(len(L)-1,0,-1):
        L[i-1],L[i]=L[i],L[i-1]
print(f"The rotated list is {L}")
'''
for i in range(0,len(L)//2):
    L[i],L[len(L)-i-1]=L[len(L)-i-1],L[i]
print(L)
for i in range(0,s//2):
    L[i],L[s-i-1]=L[s-i-1],L[i]
    print(L,"i")
print(L)
for i in range(len(L)-1,((len(L)+s)//2)-1,-1):
    L[i],L[s]=L[s],L[i]
    s+=1
    print(L,"o")
print(L)