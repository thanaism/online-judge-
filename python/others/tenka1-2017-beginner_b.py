n=int(input())
l=[[*map(int,input().split())] for _ in range(n)]
l.sort(reverse=True)
print(l[0][0]+l[0][1])