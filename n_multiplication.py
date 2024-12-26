n=int(input("Enter the number:"))
print("Multiplication of ",n,":")
for i in range(1,n+1):
    print("---------------")
    for j in range(1,11):
        print(i,"x",j,"=",i*j)