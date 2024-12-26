num1=int(input("Enter the first integer:"))
num2=int(input("Enter the second integer:"))
num3=int(input("Enter the third integer:"))
if((num1<num2<num3) or(num3<num2<num1)):
    print(num2)
elif((num2<num1<num3)or(num3<num1<num2)):
    print(num1)
else:
    print(num3)