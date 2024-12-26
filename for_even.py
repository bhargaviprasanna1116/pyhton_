n=int(input("Enter the number:"))
print("even numbers from 1 to",n,":")
#for i in range(1,n+1):
 #   if(n%2==0):
  #      print(i)
#using stepsize
for i in range(2,n+1,2):
    print(i)