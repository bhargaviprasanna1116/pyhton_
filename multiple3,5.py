n=int(input("Enter the integer:"))
if((n%3==0)and (n%5==0)):
    print(n,"is a multiple of 3 and 5")
else:
    print(n,"is not a multiple of 3 and 5")
#ternary operator
result="multiple of 3 and 5" if((n%3==0)and(n%5==0)) else "not a multiple of 3 and 5"
print(result)