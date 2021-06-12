n,m=map(int,input().split())
from collections import defaultdict
adj=defaultdict(list)
for _ in range(m):
    a,b,c,d=map(int,input().split())
    adj[a-1].append((b-1,c,d))
from heapq import heappush, heappop
INF = 10 ** 18
def dijkstra(s, n): # (始点, ノード数)
    dist = [INF] * n
    hq = [(0, s)] # (distance, node)
    dist[s] = 0
    seen = [False] * n # ノードが確定済みかどうか
    while hq:
        v = heappop(hq)[1] # ノードを pop する
        seen[v] = True
        for to, cost, delay in adj[v]: # ノード v に隣接しているノードに対して
            if seen[to] == False and dist[v] + cost + delay//(dist[v]+1) < dist[to]:
                dist[to] = dist[v] + cost + delay//(dist[v]+1)
                heappush(hq, (dist[to], to))
    return dist
dist=dijkstra(0,n)
ans=dist[n-1]
if ans==INF:ans=-1
print(ans)