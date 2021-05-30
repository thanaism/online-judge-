n=int(input())
ans='YES'
for i in range(2,n):
    if i*i>n:break
    if n%i==0:ans='NO'
print(ans)
