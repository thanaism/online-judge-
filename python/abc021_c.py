from heapq import heappush, heappop

INF = 1 << 60
MOD = 10 ** 9 + 7

def dijkstra(s, n):
    dist = [INF] * n
    num = [0] * n
    num[s] = 1
    hq = [(0, s)]  # (dist, node)
    dist[s] = 0
    seen = [False] * n
    while hq:
        v = heappop(hq)[1]
        seen[v] = True
        for to, cost in adj[v]:
            if seen[to] == False:
                if dist[v] + cost < dist[to]:
                    dist[to] = dist[v] + cost
                    num[to] = num[v]
                    heappush(hq, (dist[to], to))
                elif dist[to] == dist[v] + cost:
                    num[to] += num[v]
                    num[to] %= MOD
    return dist, num

n = int(input())
a, b = map(int, input().split())
m = int(input())
adj = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    adj[x].append((y, 1))
    adj[y].append((x, 1))
dist, num = dijkstra(a-1, n)
print(num[b - 1])
