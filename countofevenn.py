n=int(input("Enter the integer:"))
even=0
odd=0
for i in range(1,n+1):
    if(i%2==0):
        even+=1
    else:
        odd+=1
print(even,"is the count of even numbers")
print(odd,"is the count of odd numbers")