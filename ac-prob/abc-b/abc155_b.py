# n,*a=map(int,open(0).read().split())
n,a=open(0);print('ADPEPNRIOEVDE D'[any(~i&1*i%3*i%5for i in map(int,a.split()))::2])
# n,*a=map(int,open(0).read().split())
# print('DENIED'if sum([1 for i in a if ~i&1 and (i%3 and i%5)])else 'APPROVED')