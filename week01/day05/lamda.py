from functools import reduce
square=lambda a:a*a
print(square(8))

max=lambda a,b:a if a>b else b
print(max(2,3))

L=["rahul","python","ai"]
L=list(map(lambda i: str.upper(i),L))
print(L)

L=[10, 15, 20, 25, 30, 35]
print(list(filter(lambda x:  x%2!=0,L)))

L=[15, 7, 22, 10, 18]
print(reduce(lambda a,b: a if a>b else b,L))


L = [1, 2, 3, 4, 5, 6]
print(reduce(lambda a,b: a+b, map(lambda i: i*i, filter(lambda i: i%2==0,L) )))