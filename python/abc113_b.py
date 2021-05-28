n=int(input())
t,a=map(int,input().split())
h=[*map(int,input().split())]
def f(x): return abs(t-0.006*x-a)
l=f(h[0])
ans=1
for i in range(1,n):
    if f(h[i])<l:
        l=f(h[i]) 
        ans=i+1
print(ans)
