ax,ay,bx,by,cx,cy = map(int,input().split())
bx-=ax
by-=ay
cx-=ax
cy-=ay
print(0.5*abs(bx*cy-cx*by))
