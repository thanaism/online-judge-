from re import I, match
s=input()
if match(r'.*i.*c.*t.*',s,I):
    print('YES')
else:
    print('NO')