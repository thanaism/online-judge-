day=input()
l=day[:2]
if day[0]=='S':
    print(0)
else:
    a={
        'Mo':5,
        'Tu':4,
        'We':3,
        'Th':2,
        'Fr':1
    }
    print(a[l])