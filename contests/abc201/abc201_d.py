import sys
import numpy as np
from numba import njit,i8

@njit(i8(i8[:,:]),cache=True)
def solve(a):
    h,w=a.shape
    dp=np.zeros_like(a)
    dp[-1,-1]=a[-1,-1]
    if (h+w)&1==0:dp[-1,-1]*=-1
    for i in range(h-1,-1,-1):
        for j in range(w-1,-1,-1):
            if i==h-1 and j==w-1:continue
            if (i+j)&1==0:
                if j==w-1:
                    dp[i,j]=dp[i+1,j]-a[i,j]
                elif i==h-1:
                    dp[i,j]=dp[i,j+1]-a[i,j]
                else:
                    dp[i,j]=max(dp[i+1,j],dp[i,j+1])-a[i,j]
            else:
                if j==w-1:
                    dp[i,j]=dp[i+1,j]+a[i,j]
                elif i==h-1:
                    dp[i,j]=dp[i,j+1]+a[i,j]
                else:
                    dp[i,j]=min(dp[i+1,j],dp[i,j+1])+a[i,j] 
    dp[0,0]+=a[0,0]
    return dp[0,0]

def main():
    h,w=map(int,sys.stdin.buffer.readline().split())
    a=np.frombuffer(sys.stdin.buffer.read(),'a1').reshape(-1,w+1)[:,:w]
    a=np.where(a==b'+',1,-1)
    if h+w==2:
        print('Draw')
        exit()
    ans=solve(a)
    if ans>0:
        print('Takahashi')
    elif ans<0:
        print('Aoki')
    else:
        print('Draw')

if __name__=='__main__':main()