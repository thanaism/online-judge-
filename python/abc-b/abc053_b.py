s=input()
i=0
while s[i]!='A':
    i+=1
j=len(s)-1
while s[j]!='Z':
    j-=1
print(j-i+1)