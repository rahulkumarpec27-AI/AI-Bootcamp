from datetime import date
import re
dob=input("enter your dob in DD-MM-YYYY format")
today=str(date.today())
dobm=(today[5:7])
print(dobm)
doby=(today[0:4])
months=re.findall(r"-\d{2}-",dob)
print(months)
months=months[0][1:3]
print(months)
years=re.findall(r"\d{4}",dob)
if int(months)<int(dobm):
    print(years[0],doby)
    print(f"You are {int(doby)-int(years[0])} old")
else:
    print(f"You are {int(doby)-int(years[0])-1} old")

