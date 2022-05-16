a=[1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
b=[]
i=0
while i<len(a):
    if i%5==0 and i!=0:
        b.append(20)
    if i%5!=0:
        b.append(a[i])
    i=i+1
print(b)    
       
