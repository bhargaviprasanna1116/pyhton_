n=int(input("Enter the integer:"))
count=0
while(n!=0):
    n//=10
    count+=1
print("Number has",count,"digits")