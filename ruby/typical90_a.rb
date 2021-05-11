n,l=gets.split.map &:to_i
k=gets.to_s.to_i
a=gets.split.map &:to_i
ok=0
ng=l+1
def is_ok(mid,a,l,k)
    x=0
    y=0
    for i in a do
        if i-x>=mid && l-i>=mid
            x=i
            y+=1
        end
    end
    return y>=k
end
while (ng-ok).abs>1 do
    mid=(ok+ng)/2
    if is_ok(mid,a,l,k)
        ok=mid
    else
        ng=mid
    end
end
p ok
        
