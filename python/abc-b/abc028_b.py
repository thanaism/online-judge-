s=input()
l=[0]*6
for i in range(6):
    l[i]=s.count(chr(ord('A')+i))
print(*l)