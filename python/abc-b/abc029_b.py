s=[input() for _ in range(12)]
print(sum(map(lambda x:1 if 'r' in x else 0,s)))