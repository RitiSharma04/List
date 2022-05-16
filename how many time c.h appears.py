char_list=[]
numbers_of_elements=int(input("enter the numbers of elements:-"))
s=0
while s<numbers_of_elements:
    d=input("eneter the elements:-")
    char_list.append(d)
    s=s+1
list=[]
i=0
while i<len(char_list):
    if char_list[i] not in list:
        list.append(char_list[i])
    i=i+1
a=[]      
k=0
while k<len(list) :
    l=0
    count=0 
    while l<len(char_list):
        if list[k]== char_list[l]:
            count=count+1  
        else:
            count=count+0
        l+=1
    a.append([list[k],count])
    k=k+1
print(a)  


