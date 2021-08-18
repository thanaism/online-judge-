x=input()
ans='Strong'
if x[0]==x[1]==x[2]==x[3]:ans='Weak'
flg=True
for i in range(1,4):
	if int(x[i])==int(x[i-1])+1:continue
	if int(x[i])==0 and int(x[i-1])==9:continue
	flg=False
if flg:ans='Weak'
print(ans)

