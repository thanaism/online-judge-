n = int(input())
l = []
for _ in range(n-1):
    u,v,w = map(int,input().split())
    u-=1;v-=1
    l.append((w,u,v))
l.sort()

p = [-1]*n

def root(x):
    if p[x]<0: return x
    p[x] = root(p[x])
    return p[x]

def unite(x,y):
    x=root(x)
    y=root(y)
    if x<y: x,y=y,x
    p[y]+=p[x]
    p[x]=y

def size(x):
    return -p[root(x)]

ans = 0
for w,u,v in l:
    ans += w * size(u) * size(v)
    unite(u,v)

print(ans)
