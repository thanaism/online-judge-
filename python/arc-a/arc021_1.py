a=[[*map(int,input().split())] for _ in range(4)]
ok=False
for i in range(4):
    for j in range(3):
        if a[i][j]==a[i][j+1]:
            ok=True
for j in range(4):
    for i in range(3):
        if a[i][j]==a[i+1][j]:
            ok=True
if ok:
    print('CONTINUE')
else:
    print('GAMEOVER')