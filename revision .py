# #find lennth without len function

# a=[]
# b=int(input("enter the number:-"))
# i=0
# while i<=b:
#     s=int(input("enter the num:-"))
#     a.append(s)
#     i=i+1
# print(a)    
# count=0
# for i in a:
#     count=count+1
#     i=i+1
# print(count)   


# #counts the numbers between 20 and 40 



# numbers=[]
# b=int(input("enter the num:-"))
# i=0 
# while i<=b:
#     s=int(input("enter the num:-"))
#     numbers.append(s)
#     i+=1
# print(numbers)    
# count=0
# i=0
# while i<len(numbers):
#     if numbers[i]>=20 and numbers[i]<=40:
#         count=count+1
#     i=i+1
# print(count)         

# #prints the maximum in this list.
# a=[]
# b=int(input("enter the num"))
# i=0
# while i<=b:
#     s=int(input("enter the num"))
#     a.append(s)
#     i=i+1
# print(a) 
# i=0
# max=a[0]
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#     i=i+1    
# print(max)   
# #second maximum element
      
# a=[]
# b=int(input("enter the num"))
# i=0
# while i<=b:
#     s=int(input("enter the num"))
#     a.append(s)
#     i=i+1
# print(a)
# num=a[0] 
# i=0
# while i<len(a):
#     if a[i]>num:
#         num=a[i]
#     i=i+1     
# a.remove(num)
# j=0
# num1=a[0]
# while j<len(a):
#     if a[j]>num1:
#         num1=a[j]
#     j=j+1
# print(num1) 



# # print reverse order



# places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
# b=len(places)
# a=[]
# i=1
# while i==1:
#     j=b-1
#     while j>=0:
#         a.append(places[j])
#         j=j-1
#     i+=1 
# print(a)   



# #find the list is palindrome or not
  
# name=[]
# g=int(input("enter the num:-"))
# r=0
# while r<=g:
#     t=(input("enter the t:-"))
#     name.append(t)
#     r+=1
# b=len(name)
# f=[]
# s=1
# while s<=b:
#     f.append(name[b-s])
#     s=s+1
# print(f) 
# if name==f:
#     print("yes")
# else:
#     print("no")    

# #change binery to decimal

# a=[]
# num=int(input("enter the num:-"))
# i=1
# while i<=num:
#     num2=int(input("enter the num2:-"))
#     a.append(num2)
#     i=i+1
# dec=0    
# i=0
# while i<num:
#     if a[-i-1]!=0:
#         dec=dec+(2**i)
#     i=i+1
# print(a)    
# print(dec)    


# #find which numbers are not present in the second array.
 
# a=[]
# num=int(input("enter the num:-"))
# i=0
# while i<num:
#     elements=int(input("enter the elements:-"))
#     a.append(elements)
#     i=i+1
# print(a)
# b=[]
# num2=int(input("enter the num2:-"))  
# j=0
# while j<num2:
#     elements_2=int(input("enter the elements2:-"))
#     b.append(elements_2)
#     j=j+1
# print(b)    
# s=[]
# v=0
# while v<len(a):
#     if a[v] not in b:
#         s.append(a[v])
#     v=v+1
# print(s)            

    
# # alculate total marks for all the three years

   
# marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
# count=0
# j=0 
# while j<len(marks) :
#     i=0
#     while i<len(marks[j]):
#         count=count+marks[j][i]
#         i=i+1
#     j=j+1    
# print(count)   


# #example

# marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65],[95, 45, 78]]
# count=0
# i=0 
# while i<len(marks):
#     j=0
#     while j<len(marks[i]):
#         count=count+marks[i][j]
#         j=j+1
#     i=i+1
# print(count)    


# #calculate the average marks for each year

# marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
# count1=0
# count2=0
# count3=0
# i=0
# while i<len(marks):
#     j=0
#     while j<len(marks[i]):
#         if i==0:
#            count1=(count1+marks[i][j]) 
#         elif i==1:
#             count2=(count2+marks[i][j])
#         elif i==2  :
#             count3=(count3+marks[i][j])   
#         j=j+1
#     i=i+1
# print(count1/len(marks[0]))
# print(count2/len(marks[1]))
# print(count3/len(marks[2]))  



# #How to find all pairs in an array of integers whose sum is equal to the given number?


# n = [10, 11, 12, 13, 14, 17, 18, 19]
# a=[]
# b=[]
# count=0
# i=0
# while i<len(n):
#     j=0
#     while j<len(n):
#         count=n[i]+n[j]
#         if  count==30:
#             a.append([n[i],n[j]])
#         j=j+1    
#     i+=1
# b.append(a) 
# # print(b)   


# ##Magic square


# magic_square = [
# [8, 3, 4],
# [1, 5, 9],
# [6, 7, 2]]
# a=[]
# count1=0
# count2=0
# count3=0
# i=0
# while i<len(magic_square):
#     j=0
#     while j<len(magic_square[i]):
#         if i==0:
#            count1=(count1+magic_square[i][j]) 
#         elif i==1:
#             count2=(count2+magic_square[i][j])
#         elif i==2  :
#             count3=(count3+magic_square[i][j])   
#         j=j+1
#     i=i+1
# a.append([count1,count2,count3])
# b=[]
# sum=0 
# sum2=0
# sum3=0
# k=0
# while k<len(magic_square):
#     l=0
#     while l<len(magic_square[k]):
#         if l==0:
#              sum=sum+magic_square[k][l]
#         elif l==1:
#             sum2=sum2+magic_square[k][l]
#         elif l==2:
#             sum3=sum3+magic_square[k][l]
#         l=l+1
#     k=k+1
# b.append([sum,sum2,sum3])
# c=[]
# num=0
# num1=0
# m=0
# while m<len(magic_square):
#     n=0
#     while n<len(magic_square[m]):
#         if n-m==0:
#             num=num+magic_square[n][m]
#         if m+n==2:
#             num1=num1+magic_square[n][m]
#         n=n+1
#     m=m+1
# c.append([num,num1])  
# print(a)
# print(b)
# print(c)
# if a==b  :
#     print("yes")
# else:
#     print("no")    
    
            

# # make a saprate list of every first element of list
# s=[[2,3,4],[5,6,7],[3,4,5]]
# a=[]
# b=[]
# c=[]
# i=0
# while i<len(s):
#     j=0
#     while j<len(s[i]):
#         if j==0:
#             a.append(s[i][j])
#         elif j==1:
#             b.append(s[i][j])
#         elif j==2:
#             c.append(s[i][j])
#         j=j+1
#     i=i+1
# print([a,b,c])

# #odd numbers and how many even numbers are there in a given list.

# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# odd=[]
# even=[]
# i=0
# while i<len(elements):
#     if elements[i]%2!=0:
#         odd.append(elements[i])
#     else: 
#         even.append(elements[i]) 
#     i=i+1  
# print(odd)
# print(even)        


# #sum of odd numbers present in the list and the other is the sum of even numbers present in the list.

# a=[]
# b=int(input("enter the b"))
# i=0
# while i<=b:
#     c=int(input("enter the c"))
#     a.append(c)
#     i=i+1
# count_odd=0
# count_even=0
# j=0 
# while j<len(a):
#     if a[j]%2!=0:
#         count_odd=count_odd+a[j]    
#     elif a[j]%2==0:
#         count_even=count_even+a[j]
#     j=j+1        
# print("sum of odd",count_odd)
# print("sum of even",count_even)

# #average of even numbers 





# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# odd=0
# even=0
# count_odd =0
# count_even=0
# i=0
# while i<len(elements):
#     if elements[i]%2!=0:
#         odd=odd+elements[i]
#         count_odd=count_odd+i
#     else:
#         even=even+elements[i]
#         count_even=count_even+i
#     i=i+1
# print("avrage of odd","=",odd/count_odd)
# print("evrage of even","=",even/count_even)            


##odd numbers and all the even numbers and for all the numbers in the given list count,avrage ,sum

# a=[]
# b=int(input("enter the num:-"))
# i=1
# while i<b:
#     c=int(input("enter the num:-"))
#     a.append(c)
#     i=i+1    
# sum_of_odd=0
# sum_of_even=0
# count_of_odd=0
# count_of_even=0
# j=0
# while j<len(a):
#     if a[j]%2!=0:
#         sum_of_odd=sum_of_odd+a[j]
#         count_of_odd=count_of_even+j
#     else:
#         sum_of_even=sum_of_even+a[j]    
#         count_of_even=count_of_even+j
#     j=j+1
# print("sum of odd numbers","=",sum_of_odd)
# print("count of odd numbers","=",count_of_odd)
# print("avrage of odd numbers","=",sum_of_odd/count_of_odd)
# print("sum of even numbers","=",sum_of_even)
# print("count of even numbers","=",count_of_even)
# print("avrage of even numbers","=",sum_of_even/count_of_even)   



## how many people are there in the above list who are :

# kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
# Crorpati=0
# Lakhpati=0
# Diwale=0
# i=0
# while i<len(kitna_paisa_hai):
#     if kitna_paisa_hai[i]> 10000000:
#         Crorpati=Crorpati+1
#     elif kitna_paisa_hai[i]>100000:
#         Lakhpati=Lakhpati+1
#     elif kitna_paisa_hai[i]<100000:
#         Diwale=Diwale+1    
#     i=i+1
# print(Crorpati)
# print(Lakhpati)
# print(Diwale)        



## how many times a certain character or word appears.


# char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# list=[]
# i=0
# while i<len(char_list):
#     if char_list[i] not in list:
#         list.append(char_list[i])
#     i=i+1
# a=[]      
# k=0
# while k<len(list) :
#     l=0
#     count=0 
#     while l<len(char_list):
#         if list[k]== char_list[l]:
#             count=count+1  
#         else:
#             count=count+0
#         l+=1
#     a.append([list[k],count])
#     k=k+1
# print(a)    




        

            

# magic_square = [
# [8, 3, 4],
# [1, 5, 9],
# [6, 7, 2]]
# row1=0
# row2=0
# row3=0
# colum1=0 
# colum2=0
# colum3=0
# diagonal1=0
# diagonal2=0
# i=0
# while i<len(magic_square):
#     j=0
#     while j<len(magic_square[i]):
#         if i==0:
#            row1=(row1+magic_square[i][j]) 
#         elif i==1:
#             row2=(row2+magic_square[i][j])
#         elif i==2  :
#             row3=(row3+magic_square[i][j])   
#         if j==0:
#              colum1=colum1+magic_square[i][j]
#         elif j==1:
#             colum2=colum2+magic_square[i][j]
#         elif j==2:
#             colum3=colum3+magic_square[i][j]
#         if j-i==0:
#             diagonal1=diagonal1+magic_square[j][i]
#         if i+j==2:
#             diagonal2=diagonal2+magic_square[j][i]
#         j=j+1
#     i+=1        
# if row1==row2 and row1==row3 and row2==row3:
#     print([row1,row2,row3]) 
#     if colum1==colum2 and colum1==row3 and colum2==colum3:
#         print([colum1,colum2,colum3])
#         if diagonal1==diagonal2:
#             print([diagonal1,diagonal2])
#             if diagonal1==row1 and diagonal1==colum1 and row1==colum1 :
#                 print("yes")
#             else:
#                 print("no")
#         else:
#             print("NO Both diagonalare different")   
#     else:
#        print("NO Both the colum are different") 
# else:
#     print("NO Both rows are different")        
  

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
   
##debuging the problems

# marks = [10, 32, 42, 65, 67, 89, 76, 38, 67]
# total_marks = 0
# counter = 0
# while counter < len(marks):
# 	total_marks = total_marks + marks[counter]
# 	counter = counter + 1
# print(total_marks) 
   




a=["riti","saloni","pooja"]
i=0
max=len(a[0])
while i<len(a):
    if len(a[i])>max:
        max=len(a[i])
        b=a[i]
    i+=1
print(b,max)

##make a list using list constructor

# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)



# a=[[1,3,5,6],[4,2,67,8],[3,6,3,3]]
# b=[]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         b.append(a[i][j])
    
#         j=j+1
#     i=i+1        
# print(b)























        




              



