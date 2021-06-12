s=input()
l=[s[0]]
prev=0
i=1
while i<len(s):
    if l[-1]==s[prev+1:i+1]:i+=1
    l.append(s[prev+1:i+1])
    prev=i
    i+=1
ans=len(l)
if ans>1 and l[-1]==l[-2]:ans-=1
print(ans)