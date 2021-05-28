a,b,k=map(int,input().split())
cnt=0
for i in range(1+max(a,b),0,-1):
    if a%i==b%i==0: cnt+=1
    if cnt==k:
        print(i);exit()
