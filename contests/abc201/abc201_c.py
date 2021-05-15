s=input()
ans=0
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                f=True
                for m in range(10):
                    if s[m]=='o':
                        if m not in (i,j,k,l):
                            f=False
                    elif s[m]=='x':
                        if m in (i,j,k,l):
                            f=False
                if f: ans+=1
print(ans)