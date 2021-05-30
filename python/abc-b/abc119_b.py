n=int(input())
ans=0
for _ in range(n):
    i,j=input().split()
    if j=='JPY':
        ans+=int(i)
    else:
        ans+=float(i)*380000
print(ans)
    
