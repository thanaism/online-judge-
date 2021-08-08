h,w=map(int,input().split())
l=[]
for _ in range(h):
	l.append(input())
from collections import deque
q=deque()
q.append((0,0))
INF=1<<60
dist=[[INF]*w for _ in range(h)]
dist[0][0]=0
di=[-1,0,1,0]
dj=[0,1,0,-1]
dx=[-2,-2,-1,0,1,2,2,2,1,0,-1,-2,-1,1,1,-1]
dy=[0,1,2,2,2,1,0,-1,-2,-2,-2,-1,1,1,-1,-1]
while q:
	i,j=q.popleft()
	# if i==h-1 and j==w-1:break
	flg=False
	for k in range(4):
		ni=di[k]+i
		nj=dj[k]+j
		if 0<=ni<h and 0<=nj<w and dist[ni][nj]>dist[i][j] and l[ni][nj]=='.':
			dist[ni][nj]=dist[i][j]
			q.appendleft((ni,nj))
			flg=True
	# if flg:continue
	for k in range(16):
		nx=dx[k]+i
		ny=dy[k]+j
		if 0<=nx<h and 0<=ny<w and dist[nx][ny]>dist[i][j]+1:
			dist[nx][ny]=dist[i][j]+1
			q.append((nx,ny))
print(dist[h-1][w-1])

		

