n=input()
s=sum([int(c) for c in n])
if int(n)%s==0:
    print('Yes')
else:
    print('No')
