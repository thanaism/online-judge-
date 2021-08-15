from heapq import *

n = int(input())
s = [*map(int, input().split())]
t = [*map(int, input().split())]

q = []
heappush(q, n)

INF = 1<<60
dist = [INF] * (n + 1)
dist[n] = 0

while q:
    i = heappop(q)
    if i==n:
        for j in range(n):
            if dist[j]>t[j]:
                dist[j] = t[j]
                heappush(q,j)
    else:
        j = (i+1)%n
        if dist[j]>dist[i]+s[i]:
            dist[j] = dist[i]+s[i]
            heappush(q,j)
print(*dist[:n])