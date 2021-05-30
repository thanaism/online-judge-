n=int(input())
s=''
for _ in range(n):
    s+=input()
t=s.count('R')
a=s.count('B')
if t>a:
    print('TAKAHASHI')
elif a>t:
    print('AOKI')
else:
    print('DRAW')