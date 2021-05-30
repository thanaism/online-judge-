s=input()
n=int(input())
for _ in range(n):
    l,r=map(int,input().split())
    l-=1
    a=s[:l]
    b=s[l:r][::-1]
    c=s[r:]
    s=a+b+c
print(s)