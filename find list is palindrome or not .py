# places=['n', 'i', 't', 'i', 'n' ]
places="poiop"
n=list(places)
a=[]

i=1
while i<=len(places):
    a.append(places[-(i)])
    i=i+1
if n==a:
    print("yes")
else:
    print("no")




