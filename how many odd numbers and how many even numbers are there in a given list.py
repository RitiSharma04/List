a=[]
sum_of_even=0
sum_of_odd=0
size= int (input("enter the size"))
i=1
while i<=size:
    number=int(input("enter the number"))
    a.append(number)
    i=i+1  
    if number%2==0:
      sum_of_even=sum_of_even+1
    else:
       sum_of_odd=sum_of_odd+1  
print(sum_of_even)
print(sum_of_odd)
 