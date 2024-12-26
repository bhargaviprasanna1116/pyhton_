num1=int(input("Enter the first integer:"))
num2=int(input("Enter the second integer:"))
num3=int(input("Enter the third integer:"))
if(num1<num2 and num1<num3):
    print(num1)
elif(num2<num1 and num2<num3):
    print(num2)
else:
    print(num3)
#ternary operator
result2=num2 if(num2<num1 and num2<num3) else num3
result1= num1 if(num1<num2 and num1<num3) else result2
if(result1==result2):
    print(result1)
else:
    print(result2)