n=int(input())
a,b=map(int,input().split())
k=int(input())
p=[*map(int,input().split())]
ans='YES'
if a in p:ans='NO'
if b in p:ans='NO'
for i in p:
    if p.count(i)>1:ans='NO'
print(ans)