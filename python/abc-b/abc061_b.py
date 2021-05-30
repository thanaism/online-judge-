n,m=map(int,input().split())
l=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    l[a-1].append(b-1)
    l[b-1].append(a-1)
for k in l:
    print(len(k))