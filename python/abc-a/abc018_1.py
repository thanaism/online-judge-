a=int(input())
b=int(input())
c=int(input())
l=[a,b,c]
for i in l:
    if i==max(l):
        print(1)
    elif i==min(l):
        print(3)
    else:
        print(2)