n=int(input("Enter the integer:"))
if((n>9999 and n<=99999)or (n>=-99999 and n<-9999)):
    print("It is a five digit number")
else:
    print("It is not a five digit number")