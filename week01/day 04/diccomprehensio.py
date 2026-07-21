dict1={i:i*10 for i in range(1,6)}
print(dict1)

dict1={"Rahul" :"kumar", "job":"AI Engineer"}
dict2={}
dict1={key:value for value,key in dict1.items()}
print(f"Swapped is {dict1}")