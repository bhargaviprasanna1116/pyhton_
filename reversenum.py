n=int(input("enter the number:"))
rem=0
reversed_num=0
while(n!=0):
    rem=n%10
    reversed_num=reversed_num*10+rem
    n//=10
print("Reversed number is:",reversed_num)