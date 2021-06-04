n=int(input())
a,b=map(int,input().split())
p=[*map(int,input().split())]
i=sum([1 for i in p if i<=a])
j=sum([1 for i in p if a<i<=b])
k=sum([1 for i in p if i>b])
print(min(i,j,k))