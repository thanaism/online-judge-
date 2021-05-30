n=int(input())
total=0
for i in range(1,10):
    for j in range(1,10):
        total+=i*j
diff=total-n
for i in range(1,10):
    if diff%i==0 and 1<=diff//i<=9:
        print(f'{i} x {diff//i}')