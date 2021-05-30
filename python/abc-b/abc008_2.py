n=int(input())
s=[input() for _ in range(n)]
from collections import Counter
print(max(Counter(s).items(),key=lambda x:x[1])[0])