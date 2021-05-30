l=[*input().split()]
ans=[]
for w in l:
    if w=='Right':
        ans.append('>')
    if w=='Left':
        ans.append('<')
    if w=='AtCoder':
        ans.append('A')
print(*ans)