n=int(input())
a=[*map(int,input().split())]
a.sort(reverse=True)
print(sum(a[::2]))