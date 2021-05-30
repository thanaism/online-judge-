s=input()
k=int(input())
t=set()
for i in range(len(s)):
    if i+k<=len(s):
        t.add(s[i:i+k])
print(len(t))