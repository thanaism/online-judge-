s=input()
k=int(input())
num=0
for c in s:
	if c=='1':
		num+=1
	else:
		ans=c
		break
if num>=k: ans=1
print(ans)