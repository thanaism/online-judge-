n=int(input())
s=set()
prev=input()
s.add(prev)
for _ in range(1,n):
    w=input()
    if prev[-1]==w[0] and w not in s:
        s.add(w)
        prev=w
        continue
    print('No');exit()
print('Yes')


