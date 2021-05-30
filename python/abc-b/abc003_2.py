s=input()
t=input()
for i in range(len(s)):
    if s[i]==t[i]:continue
    elif s[i]=='@' and t[i] in '@atcoder':continue
    elif t[i]=='@' and s[i] in '@atcoder':continue
    else:
        print('You will lose')
        exit()
print('You can win')