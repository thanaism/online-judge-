n, k = map(int, input().split())
a = [*map(int, input().split())]
for i in range(k, n):
    print("Yes" if a[i] > a[i - k] else "No")
