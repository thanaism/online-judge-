n=int(input())
s=input()
a='b'
i=0
while len(a)<n:
    i+=1
    if i%3==1:
        a='a'+a+'c'
    elif i%3==2:
        a='c'+a+'a'
    elif i%3==0:
        a='b'+a+'b'
if s==a:
    print(i)
else:
    print(-1)