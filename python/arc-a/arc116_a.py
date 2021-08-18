t=int(input())
for _ in range(t):
    n=int(input())
    d=(n&-n)-1
    if d==1:
        print('Same')
    elif d>1:
        print('Even')
    else:
        print('Odd')