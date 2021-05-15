h,w=map(int,input().split())
grid=[]
for _ in range(h):
    grid.append(input())
dp = [ [0]*(w+10) for _ in range(h+10)]
for i in range(h):
    for j in range(w):
            l=[]
            # if j>=2: l.append(dp[i][j-2])
            # if i>=2: l.append(dp[i-2][j])
            # if i>=1 and j>=1: l.append(dp[i-1][j-1])
            if dp[i-1][j]==dp[i][j-1]:
                l.append(dp[i][j-2])
                l.append(dp[i-2][j])
            elif dp[i-1][j]>dp[i][j-1]:
                l.append(dp[i-2][j])
            else:
                l.append(dp[i][j-2]) 
            l.append(dp[i-1][j-1])
            # if len(l)>0:
            if i==j==0:
                continue
            else:
                if grid[i][j]=='-':
                    dp[i][j]=max(l)-1
                else:
                    dp[i][j]=max(l)+1
if ~(((h-1)&1)^((w-1)&1)):
    # Takahashi
    l=[]
    if w-1>0: l.append(dp[h-1][w-2])
    if h-1>0: l.append(dp[h-2][w-1])
    if len(l)==0:
        print('Draw')
    elif dp[h-1][w-1]>max(l):
        print('Aoki')
    elif dp[h-1][w-1]==max(l):
        print('Draw')
    else:
        print('Takahashi')
else:
    # Aoki
    l=[]
    if w-1>0: l.append(dp[h-1][w-2])
    if h-1>0: l.append(dp[h-2][w-1])
    if dp[h-1][w-1]>max(l):
        print('Takahashi')
    elif dp[h-1][w-1]==max(l):
        print('Draw')
    else:
        print('Aoki')

# for i in range(h):
    # print(dp[i][:w])