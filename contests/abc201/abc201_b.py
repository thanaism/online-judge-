n=int(input())
l=[]
for _ in range(n):
    s,t=input().split()
    l.append((s,int(t)))
l.sort(key=lambda x: x[1])
print(l[-2][0])