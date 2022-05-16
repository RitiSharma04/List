n=int(input("enter the numbert"))
b=0
i=1
while i<=10:
    if n%i==0:
         b=b+1
    i=i+1 
if b==2:
    print("it is a prime number")
else:
    print("it is not prime")    

