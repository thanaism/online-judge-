a,b,c=map(int,input().split())
MOD=10**9+7
a%=MOD
b%=MOD
c%=MOD
print(a*b*c%MOD)