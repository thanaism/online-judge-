n,l=gets.split.map(&:to_i)
k=gets.to_s.to_i
a=gets.split.map(&:to_i)
p a.sort().bsearch{|i|i<k}
print a