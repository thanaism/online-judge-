n=int(input())
if n==1:print(0);exit()
p=[True]*(n)
p[0]=False
p[1]=False
for i in range(2,n):
    if p[i]:
        for j in range(i+i,n,i):
            p[j]=False
print(sum([1 for i in p if i]))