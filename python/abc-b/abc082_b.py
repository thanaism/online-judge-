s=[c for c in input()]
t=[c for c in input()]
s.sort()
t.sort(reverse=True)
if ''.join(s)<''.join(t):
    print('Yes')
else:
    print('No')