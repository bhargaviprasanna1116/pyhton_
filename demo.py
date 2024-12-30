#double quotes
name="bhargavi"
print(name)
print(type(name))
print("----------------")
#single quotes
name='madhu'
print(name)
print(type(name))
#triple single quotes
print("-----------------")
name='''hanu'''
print(name)
print(type(name))
print("------------------")
#triple double quotes
name="""bhanu"""
print(name)
print(type(name))
print("-------------------")
#double within single quotes
name="bhanu is 'dancing'"
print(name)
print(type(name))
print("--------------------")
#single within double quotes
name='sandhya is "dancing"'
print(name)
print(type(name))
print("--------------------")
#escape character
name="hi \n Had dinner?"
print(name)
print(type(name))
print("--------------------")
#raw string
name=r"ramya is dancing"
print(name)
print(type(name))
#membership operators
n=[1,2,3,4,5]
print(2 in n)
st="i am bhavi"
print("am" in st)
print("is" not in st)
#delete operation
del n[2],n[3]
print(n)
s=["hi","hlo","go","no"]
for i in range(len(s)):
    print(s[i])
print("------------")
for i in s:
    print(i)
print("--------------")
#mutlidimensional list
num=[[1,2,3],[4,5,6],[7,8,9]]
print(num)
print(num[0])
print(num[0][0])
print(num[0][1])
print(num[0][2])
print(num[1])
print(num[1][0])
print(num[1][1])
print(num[1][2])
print(num[2])
print(num[2][0])
print(num[2][1])
print(num[2][2])