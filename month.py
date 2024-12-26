month=int(input("Enter the month number:"))
if(month>=1 and month<=12):
    print("Valid month")
else:
    print("In-valid month")
#ternary operator
result="valid month" if(month>=1 and month<=12) else "In-valid month"
print(result)