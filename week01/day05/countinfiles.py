from functools import reduce
try:
    with open("articles.txt","r") as f:
        countcharacters=len(f.read())
        f.seek(0)
        countlines=len(f.readlines())
        f.seek(0)
        L=f.readlines()
        countwords=reduce(lambda a,b: a+b, list(map(lambda i: len(i.split()),L)))
        f.close()
        print(f" Number of characters are : {countcharacters}")
        print(f" Number of words are : {countwords}")
        print(f" Number of lines are : {countlines}")
except FileNotFoundError:
    print("file does not exist")

a,b=2,3
b=a+b
a=b-a
b=b-a
print(a,b)