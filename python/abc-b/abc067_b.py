n,k=map(int,input().split())
l=[*map(int,input().split())]
l.sort(reverse=True)
print(sum(l[:k]))