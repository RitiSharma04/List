##Take out the duplicates from this list and put it in different list and print it.e

# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# newA=[]
# i=0
# while i<len(n):
#     j=i
#     while j<len(n):
#         if n[i]==n[j]:
#             if n[i] not in newA:
#                 k=n[i]
#                 newA=newA+[k]
#         j+=1
#     i+=1
# print(newA)   



# list=[]
# a=int(input("enter the numbers:-"))
# i=0
# while i<a:
#     b=int(input("enter the number:-"))
#     list.append(b)
#     i=i+1
# print(list)
# r=[] 
# f=[]   
# j=0
# while j<len(list):
#     if list[j] not in r:
#         r.append(list[j])
#     else:
#         f.append(list[j])   
#     j=j+1
# print(f)

n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
newA=[]
i=0
while i<len(n):
    if n[i] not in newA:
        k=n[i]
        newA=newA+[k]
    i+=1
print(newA)