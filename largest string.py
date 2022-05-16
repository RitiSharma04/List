a=["riti","saloni","pooja"]
i=0
l=[]
max=len(a[0])
while i<len(a):
    if len(a[i])>max:
        max=len(a[i])
        b=a[i]
    i+=1
print(max)
print(b)