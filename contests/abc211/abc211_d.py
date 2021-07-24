from heapq import heappush, heappop
INF = 1<<60
MOD = 10**9+7

def dijkstra(s, n):
	dist = [INF] * n
	num = [0] * n
	num[0]=1
	hq = [(0, s)] # (distance, node)
	dist[s] = 0
	seen = [False] * n # ノードが確定済みかどうか
	while hq:
		v = heappop(hq)[1] # ノードを pop する
		seen[v] = True
		for to, cost in adj[v]: # ノード v に隣接しているノードに対して
			if seen[to] == False:
				if dist[v] + cost < dist[to]:
					dist[to] = dist[v] + cost
					num[to] = num[v]
					heappush(hq, (dist[to], to))
				elif dist[to] == dist[v] + cost:
					num[to] += num[v]
					num[to] %= MOD
	return dist,num

n,m=map(int,input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
	a,b=map(int,input().split())
	a-=1;b-=1
	adj[a].append((b,1))
	adj[b].append((a,1))
dist,num=dijkstra(0,n)
print(num[n-1])