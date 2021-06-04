n=int(input())
a=[*map(int,input().split())]
def f(x):
    res=0
    while True:
        if x%2!=0:break
        x//=2
        res+=1
    return res

b=[f(i) for i in a]
print(sum(b))