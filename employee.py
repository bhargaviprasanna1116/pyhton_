name=input("Enter employee name:")
desi=input("Enter Designation:")
sal=int(input("Enter your salary:"))
spl_allow=int(input("Enetr amount of special allowance:"))
bonus=int(input("Enter ammount of bonus:"))
gr_mon=sal+spl_allow
print("Gross Monthly salary:",gr_mon)
gr_anl=((gr_mon*12)+bonus)
print("Gross Annual Salary:",gr_anl)
if(gr_anl>500000):
    tx=((gr_anl*15)/100)
    print("Taxable income is:",gr_anl-tx)
elif((gr_anl*10)/100):
    tx=((gr_anl*12)+bonus)
    print("Taxable income is:",gr_anl-tx)
else:
    tx=((gr_anl*12)+bonus)
    print("Taxable income is:",gr_anl-tx)