n=int(input())
if n==1:
    print('BOWWOW')
    exit()
n=(n+1)*n//2
for i in range(2,n+1):
    if i*i>n:break
    if n%i==0:
        print('BOWWOW')
        exit()
print('WANWAN')