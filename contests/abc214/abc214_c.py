n=int(input())
s=[*map(int,input().split())]
t=[*map(int,input().split())]
x=t.index(min(t))
for i in range(n*2):
	j=(i+1)%n
	t[j]=min(t[j],t[i%n]+s[i%n])
for i in t:
	print(i)
