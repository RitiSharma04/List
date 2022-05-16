a=[4,56,34,65,34,5,4,6,7,5,75,45,78,9,9]
b=int(input("enter the number:-"))
repitetion=0
for i in range(len(a)):
    if b==a[i]:
        repitetion=repitetion+1
print(repitetion)        