s=input()
w=int(input())
ans=''
while len(s)>0:
    ans+=s[0]
    s=s[w:]
print(ans)