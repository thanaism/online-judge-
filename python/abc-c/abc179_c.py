n = int(input())
ans = 0
for i in range(1, n + 1):
    ans += (n - 1) // i
print(ans)
