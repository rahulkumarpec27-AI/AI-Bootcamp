#All exception handler
'''try:
    a=int(input("Enter the first number"))
    b=int(input("Enter the second number"))
    div=a/b

except Exception as e:
    print(type(e))
    print(e)     

else:
    print(f"output is {div}")

except ValueError:
    print("Please enter integer only")
    
except ZeroDivisionError:
    print("cannot divide by 0")

#index out of range
L=[10, 20, 30, 40]
try:
    index=int(input("kindly enter the index"))
    print(L[index])
except IndexError:
    print("Index is out of range")
except ValueError:
    print("Please enter a valid integer index.")

#key not found in dictionary
student = {
    "name": "Rahul",
    "age": 25,
    "city": "Delhi"
}

key=input("please enter the key")
try:
    print(student[key])
except KeyError:
    print("Key does not exist.")

#raise exception
a=int(input("enter the value"))
if a<0:
    raise ValueError("Kindly enter only positive number")
else:
    print(f"Number entered is {a}")'''

class NegativeAgeError(Exception):
    pass
age=int(input("kindly enter your age"))
if age<0:
    raise NegativeAgeError("kindly enter age in positive numbers only")