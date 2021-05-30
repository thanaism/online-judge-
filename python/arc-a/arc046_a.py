n=int(input())
i=0
j=1
while i<n:
    s=str(j)
    if all(map(lambda x:x==s[0],s)):
        i+=1
    j+=1
print(s)