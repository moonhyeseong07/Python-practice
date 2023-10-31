n=input()
a=n[::-1]
sum=str(int(n)+int(a))
if sum==sum[::-1]:
    print('YES')
else: print('NO')
