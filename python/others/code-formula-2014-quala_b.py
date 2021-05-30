a,b=map(int,input().split())
p=[*map(int,input().split())]
q=[*map(int,input().split())]
l=[]
l.append('7 8 9 0')
l.append(' 4 5 6')
l.append('  2 3')
l.append('   1')
for i in range(10):
    if i in p:
        for j in range(4):
            l[j]=l[j].replace(str(i),'.')
    if i in q:
        for j in range(4):
            l[j]=l[j].replace(str(i),'o')
for i in range(4):
    for j in range(10):
        l[i]=l[i].replace(str(j),'x')
    print(l[i])
