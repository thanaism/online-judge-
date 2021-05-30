y=int(input())
m=int(input())
d=int(input())
if 1<=m<=2:
    m+=12
    y-=1
def p(y,m,d):
    ans=365*y
    ans+=y//4
    ans-=y//100
    ans+=y//400
    ans+=306*(m+1)//10
    ans+=d
    ans-=429
    return ans
print(p(2014,5,17)-p(y,m,d))