a=[2,5,34,6,5,4,6]
sum_of_even=0
product_of_odd=1
for i in range(len(a)):
    if a[i]%2==0:
        sum_of_even=sum_of_even+a[i]
    else:
        product_of_odd=product_of_odd*a[i]
print(sum_of_even)
print(product_of_odd)            
