n=int(input())
l=[]
l.append(2)
l.append(1)
i=1
while i<n:
    l.append(l[i]+l[i-1])
    i+=1
print(l[n])