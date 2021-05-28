n=int(input())
for i in range(n,1000):
    s=str(i)    
    if all(map(lambda x:x==s[0],s)):
        print(i);break
    
