for i in range(101,1000):
    n=i
    reversed_num=0
    rem=0
    while(i!=0):
        rem=i%10
        reversed_num=reversed_num*10+rem
        i//=10
    if(reversed_num==n):
        print(reversed_num)
#without loop statements
for i in range(1,10):
    for j in range(0,10):
        print(i,j,i)