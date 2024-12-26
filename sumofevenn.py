n=int(input("Enter the integer:"))
even=0
odd=0
for i in range(1,n+1):
    if(i%2==0):
        even+=i
    else:
        odd+=i
print(even,"is the sum of even numbers ")
print(odd,"is the sum of odd numbers")