n=int(input("enter the number:"))
rem=0
num=n
reversed_num=0
while(n!=0):
    rem=n%10
    reversed_num=reversed_num*10+rem
    n//=10
if(reversed_num==num):
    print(num,"is a palindrome number.")
else:
    print(num,"is not a palindrome")