n=int(input())
ans=n//10*100+n%10*15
ans=min(ans,(n+9)//10*100)
print(ans)