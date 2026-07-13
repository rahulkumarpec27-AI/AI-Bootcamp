num=int(input("enter the pattern range"))
for i in range (0,num):
    print("*",end='')
for j in range(0,num-2,1):
    print()
    print("*",end='')
    for i in range (num-1,1,-1):
        print(" ",end='')
    print("*",end='')
print()
for i in range (0,num):
    print("*",end='')
