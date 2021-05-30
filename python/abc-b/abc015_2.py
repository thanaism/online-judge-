n=int(input())
a=[*map(int,input().split())]
print(-(-sum(a)//sum([1 for i in a if i>0])))