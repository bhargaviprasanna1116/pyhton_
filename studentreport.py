name=input("Enter student name:")
s1=int(input("Enter subject1 score:"))
s2=int(input("Enter subject2 score:"))
s3=int(input("Enter subject3 score:"))
print("STUDENT REPORT CARD")
print("--------------------")
print("Student Name:",name)
print("Subject1 Score:",s1)
print("Subject2 score:",s2)
print("Subject3 score:",s3)
avg=((s1+s2+s3)/3)
if((s1>=35)and(s2>=35)and(s3>=35)):
    print("Total:",s1+s2+s3)
    print("Average:",avg)
    if(avg>90):
        print("congratulations you have qualified with 1st class")
    elif(avg>75):
        print("congratulations you have qualified with 2nd class")
    else:
        print("congratulations you have qualified with 3rd class")
else:
    print("you are not qualified.")
