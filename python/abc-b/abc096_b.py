a,b,c=map(int,input().split())
k=int(input())
print((max(a,b,c)<<k)+a+b+c-max(a,b,c))