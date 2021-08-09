h,w,c=map(int,input().split())
l=[]
INF=1<<60
for _ in range(h):
    l.append(list(map(int,input().split())))

def solve():
    mi = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            mi[i][j]=l[i][j]-c*(i+j)

    for i in range(h):
        for j in range(w):
            if i>0:mi[i][j]=min(mi[i][j],mi[i-1][j])
            if j>0:mi[i][j]=min(mi[i][j],mi[i][j-1])
    
    res=INF
    for i in range(h):
        for j in range(w):
            opt=INF
            if i>0:opt=min(opt,mi[i-1][j])
            if j>0:opt=min(opt,mi[i][j-1])
            res=min(res,l[i][j]+c*(i+j)+opt)
    
    return res

def rotate(l,h,w):
    g=[[0]*h for _ in range(w)]
    for i in range(h):
        for j in range(w):
            g[j][h-i-1]=l[i][j]
    return g,w,h


ans=solve()
l,h,w=rotate(l,h,w)
ans=min(ans,solve())
print(ans)

