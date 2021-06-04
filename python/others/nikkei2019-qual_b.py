n=int(input())
a=input()
b=input()
c=input()
ans=0
for i,j,k in zip(a,b,c):
    if i==j==k:continue
    elif i==j:ans+=1
    elif j==k:ans+=1
    elif k==i:ans+=1
    else:ans+=2
print(ans)    

