num1=int(input("Enter the frist integer :"))
num2=int(input("Enter the second integer:"))
if(num1==num2):
    print("Two integers are equal")
else:
    print("Two integers are not equal")
#ternary operator
result="Two integers are equal" if(num1==num2) else "Two integers are not equal"
print(result)