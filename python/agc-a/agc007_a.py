h,w=map(int,input().split())
grid=[input() for _ in range(h)]
used=[[False]*w for _ in range(h)]
from collections import deque
que=deque()
que.append((0,0))
di=[0,1]
dj=[1,0]
while que:
    i,j=que.popleft()
    used[i][j]=True
    for k in range(2):
        ni=i+di[k]
        nj=j+dj[k]
        if 0<=ni<h and 0<=nj<w:
            if grid[ni][nj]=='#' and not used[ni][nj]:
                que.append((ni,nj))
                break
ok=True
for i in range(h):
    for j in range(w):
        if grid[i][j]=='#' and not used[i][j]:
            ok=False

if ok:
    print('Possible')
else:
    print('Impossible')