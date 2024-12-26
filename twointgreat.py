num1=int(input("Enter the frist integer:"))
num2=int(input("Enter the second integer:"))
if(num1>num2):
    print(num1)
else:
    print(num2)
#ternary operator
result= num1 if(num1>num2) else num2
print(result)