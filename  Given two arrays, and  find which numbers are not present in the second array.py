a=[]
size=int(input("enter the size"))
i=1
while i<=size:
    list=int(input("enter the list"))
    a.append(list)
    i=i+1
print(a)   
b=[]
size2=int(input("enter the size"))
l=1
while l<=size2:
    list2=int(input("enter the list"))
    b.append(list2)
    l=l+1
print(b)   
# list1 = [1,2,3,4,5,6]
# list2 = [2,3,1,0,6,7]
s=[]
for i in a:
    if i not in b:
        s.append(i)
print(s)





























