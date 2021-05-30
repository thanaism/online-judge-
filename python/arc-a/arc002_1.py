y=int(input())
flg=True
if y%4!=0:
    flg=False
elif y%400!=0 and y%100==0:
    flg=False
if flg:
    print('YES')
else:
    print('NO')
