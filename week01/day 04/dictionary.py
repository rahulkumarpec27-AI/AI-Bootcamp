'''key,value=(input("enter the first dictionary key value pair").split(":"))
d1={key:value}
key,value=(input("enter the second dictionary key value pair").split(":"))
d2={key:value}
for i in d1:
    d2[i]=d1[i]
print(f"merged dictionary is {d2}")
'''

str1=input("Enter your string")
dict1={}
for i in str1:
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i]=1
print(f"\nFrequency is {dict1}")