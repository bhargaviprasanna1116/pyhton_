str=input("Enter the string:")
v_count=0
c_count=0
for i in str:
    if(i in ('A','E','I','O','U','a','e','i','o','u')):
        v_count+=1
    elif((i.isalpha())):
        c_count+=1
print("Vowel count:",v_count)
print("Consonant count:",c_count)