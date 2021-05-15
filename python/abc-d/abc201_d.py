"""TLE"""
# h,w=map(int,input().split())
# if h+w==2:
#     print('Draw');exit()
# l=[]
# for _ in range(h):l.append(input())
# dp=[[0]*w for _ in range(h)]
# dp[0][0]+=eval(l[0][0]+'1')
# if (h+w)&1==0:dp[-1][-1]*=-1
# def x(i,j,k,f):
#     k=eval(l[i][j]+'1')*k
#     if j==w-1:
#         dp[i][j]=dp[i+1][j]-k
#     elif i==h-1:
#         dp[i][j]=dp[i][j+1]-k
#     else:
#         dp[i][j]=f(dp[i+1][j],dp[i][j+1])-k
# for i in reversed(range(h)):
#     for j in reversed(range(w)):
#         if i==h-1 and j==w-1:continue
#         if (i+j)&1==0: x(i,j,1,max)
#         else: x(i,j,-1,min)
# if dp[0][0]>0:
#     print('Takahashi')
# elif dp[0][0]<0:
#     print('Aoki')
# else:
#     print('Draw')
h,w=map(int,input().split())
if h+w==2:
    print('Draw')
    exit()
l=[]
for _ in range(h):
    l.append(list(input()))
for i in range(h):
    for j in range(w):
        if l[i][j]=='+':l[i][j]=1
        if l[i][j]=='-':l[i][j]=-1
dp=[[0]*w for _ in range(h)]
dp[0][0]+=l[0][0]
if (h+w)&1==0:dp[-1][-1]*=-1
def func(i,j,k,f):
    if j==w-1:
        dp[i][j]=dp[i+1][j]-k
    elif i==h-1:
        dp[i][j]=dp[i][j+1]-k
    else:
        dp[i][j]=f(dp[i+1][j],dp[i][j+1])-k
for i in reversed(range(h)):
    for j in reversed(range(w)):
        if i==h-1 and j==w-1:continue
        if (i+j)&1==0: func(i,j,l[i][j],max)
        else: func(i,j,-l[i][j],min)
if dp[0][0]>0:
    print('Takahashi')
elif dp[0][0]<0:
    print('Aoki')
else:
    print('Draw')