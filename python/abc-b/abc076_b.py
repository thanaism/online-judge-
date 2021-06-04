n=int(input())
k=int(input())
x=1
i=0
while x<k and i<n:
    x*=2
    i+=1
while i<n:
    x+=k
    i+=1
print(x)