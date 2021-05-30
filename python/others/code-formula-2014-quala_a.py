a=int(input())
ans='NO'
for i in range(101):
    if i**3==a:
        ans='YES'
        break
print(ans)