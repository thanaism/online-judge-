s=input()
ans=[]
for c in s:
    a=c
    if c=='6': a='9'
    elif c=='9': a='6'
    ans.append(a)
print(''.join(reversed(ans)))