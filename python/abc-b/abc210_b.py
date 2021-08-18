n=int(input())
s=input()
for i in range(n):
	if s[i]=='1':
		if i&1:
			print('Aoki')
		else:
			print('Takahashi')
		break