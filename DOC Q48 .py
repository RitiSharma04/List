a=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
b=int(input("enter the number:-"))
d=[]
j=0
while j<len(a):
    c=[]
    i=0
    while i<j+b:
        c.append(a[i])
        i=i+1
    d.append(c)    
    j=j+1
print(d)        


    
    


    
