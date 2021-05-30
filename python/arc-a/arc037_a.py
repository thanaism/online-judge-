n=int(input())
m=[*map(int,input().split())]
print(sum(map(lambda x:max(0,80-x),m)))