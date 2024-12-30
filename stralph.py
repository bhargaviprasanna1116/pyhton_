n=input("Enter the string:")
d_count=0
a_count=0
s_count=0
for i in n:
    if(i.isalpha()):
        a_count+=1
    elif(i.isnumeric()):
        d_count+=1
    elif(i.isspace()):
        continue
    else:
        s_count+=1
print("Nuber of digits in string are:",d_count)
print("Number of alphabets in string are:",a_count)
print("Number of special characters in string are:",s_count)