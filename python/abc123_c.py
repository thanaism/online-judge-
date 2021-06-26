n=int(input())
l=[int(input()) for _ in range(5)]
ll=min(l)
for i in range(5):
	if l[i]==ll:
		idx=i
		break
ans=(n+ll-1)//ll
print(ans+4)