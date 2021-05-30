s=input()
l=[int(c) for c in s]
a=sum(l[::2])
b=sum(l[1::2])
print(a-b)