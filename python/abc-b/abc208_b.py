p=int(input())
l=[1]
for i in range(2,11):
	l.append(l[-1]*i)
ans=0
for i in reversed(l):
	ans+=(p//i)
	p%=i
print(ans)