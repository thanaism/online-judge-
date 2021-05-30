s=input()
m={
    'O':'0',
    'D':'0',
    'I':'1',
    'Z':'2',
    'S':'5',
    'B':'8'
}
ans=''
for c in s:
    if c in m:
        ans+=m[c]
    else:
        ans+=c
print(ans)