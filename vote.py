Age=int(input("enter your age:"))
if(Age<18):
    print("you are not eligible to vote")
else:
    print("you are eligible to vote")
#ternary operator
result="you are eligible to vote" if(Age>=18) else "you are not eligible to vote"
print(result)