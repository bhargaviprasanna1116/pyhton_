n=int(input("enter the integer:"))
even=0
odd=0
while(n!=0):
    rem=n%10
    if(rem%2==0):
        even+=1
    else:
        odd+=1
    n=n//10
print("Number of even digits are",even)
print("Number of odd digits are",odd)