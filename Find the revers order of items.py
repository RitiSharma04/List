places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
i=0
j=len(places)-1
while i<j:
    t=places[i]
    places[i]=places[j]
    places[j]=t
    i=i+1
    j=j-1
print(places)




