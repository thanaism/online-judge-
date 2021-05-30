n=int(input())
ans=1<<60
for i in range(1,10**5+1):
    ans=min(ans,n-(n//i)*i+abs(i-n//i))
print(ans)
