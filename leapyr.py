year=int(input("Enter the year:"))
if((year%4==0)and((year%100!=0)or(year%400==0))):
    print("20 leap years from",year)
    for i in range(1,21):
        print(year+4)