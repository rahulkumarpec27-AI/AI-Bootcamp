from datetime import date
import re
dob=input("enter your dob in DD-MM-YYYY format")
today=str(date.today())
dobm=(today[5:7])
doby=(today[0:4])
months=re.findall(r"-\d{2}-",dob)
months=months[0][1:3]
years=re.findall(r"\d{4}",dob)
if int(months)>int(dobm):
    month=(12-int(months)+int(dobm))
    print(f"You are {month} months {int(doby)-int(years[0])-1} years old")
else:
    month=int(dobm)-int(months)
    print(f"You are {month} months {int(doby)-int(years[0])} years old")

