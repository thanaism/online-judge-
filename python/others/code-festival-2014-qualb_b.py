n,k=map(int,input().split())
s=0
for i in range(n):
    s+=int(input())
    if s>=k:
        print(i+1)
        exit()