year=int(input("Enter the year:"))
count=20
leap_count=0
while(leap_count!=count):
    if((year%4==0)and((year%100!=0)or(year%400==0))):
        leap_count+=1
        print(year)
    year+=1