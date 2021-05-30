s=input()
ok=True
for i in range(len(s)):
    if s[i]==s[-i-1] or s[i]=='*' or s[-i-1]=='*':
        continue
    else:
        ok=False
if ok:
    print('YES')
else:
    print('NO')