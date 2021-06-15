a,b,c=map(int,input().split())
if c%2==0:
	# 正負関係なし
	if abs(a)<abs(b):
		print('<')
	elif abs(a)==abs(b):
		print('=')
	elif abs(a)>abs(b):
		print('>')
elif c%2==1:
	if (a<0)^(b<0):
		# 正負が一致しないなら負の数が必ず小さい
		if a<0:print('<')
		else:print('>')
	# 正負が一致するなら、正負で結果が反転
	elif a<0:
		if abs(a)<abs(b):
			print('>')
		elif abs(a)==abs(b):
			print('=')
		elif abs(a)>abs(b):
			print('<')	
	else:
		if abs(a)<abs(b):
			print('<')
		elif abs(a)==abs(b):
			print('=')
		elif abs(a)>abs(b):
			print('>')

