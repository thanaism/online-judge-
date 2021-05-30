n=int(input())
a=[*map(int,input().split())]
s=0
for i in a:
    s*=2
    s+=i
print(s)