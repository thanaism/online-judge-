a=[1]+[0]*8
s="chokudai"
for c in input():
 for i in range(8):a[i+1]+=a[i]*(s[i]==c)
print(a[8]%(10**9+7))