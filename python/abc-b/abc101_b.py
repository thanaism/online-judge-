n=input()
m=sum([int(c) for c in n])
if int(n)%m==0:
    print('Yes')
else:
    print('No')