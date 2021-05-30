h,w=map(int,input().split())
s=[]
for _ in range(h):
    s.append(input())
print('#'*(w+2))
for l in s:
    print('#'+l+'#')
print('#'*(w+2))
