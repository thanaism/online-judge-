s=input()
ans='YES'
for i in range(len(s)):
    if s[i]!=s[-i-1]:
        ans='NO'
        break
print(ans)