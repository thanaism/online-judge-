a,b=map(int,input().split())
c,d=map(int,input().split())
e,f=map(int,input().split())
l=[a,b,c,d,e,f]
m=[]
for i in l:
    m.append(l.count(i))
m.sort()
if m==[1,1,2,2,2,2]:
    print('YES')
else:
    print('NO')