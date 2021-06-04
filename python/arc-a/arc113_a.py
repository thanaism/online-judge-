k=int(input())
def div(x):
    res=dict()
    n=x
    for d in range(2,x+1):
        if d*d>x:break
        cnt=0
        while True:
            if n%d!=0:break
            n//=d
            cnt+=1
            res[d]=cnt
    if n!=1:res[n]=1
    return res
ans=0
for i in range(1,k+1):
    dic=div(i)
    l=[1]
    for key,val in dic.items():
        l.append(l[-1]*(val+2)*(val+1)//2)
    ans+=l[-1]
print(ans)
