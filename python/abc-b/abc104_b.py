s=input()
if s[0]=='A'and s[2:-1].count('C')==1:
    t=s[1]+s[2:-1].replace('C','')+s[-1:]
    if t==t.lower():
        print('AC')
        exit()
print('WA')