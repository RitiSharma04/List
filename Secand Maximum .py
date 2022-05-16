a=[10,20,30,100,40,50,60,700,80,90]
# max=a[0]    
# second_max=a[0]   
# for i in range(len(a)):
#     if a[i]>max:
#         max=a[i]
# a.remove(max)
# for v in range(len(a)):
#     if a[v]>second_max:
#         second_max=a[v]       
# print(second_max)        



b=a[0]
for i in range(0,len(a)-1):
    if a[i]>b:
        b=a[i]
# print(b)    
c=a[0]
for i in range(0,len(a)-1):
    if a[i]>c and c<b:
        c=a[i]
print(c)            