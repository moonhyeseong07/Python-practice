n=int(input())
prime=True
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        prime=False
        break
if prime and n>=2:
    print("prime")
else:
    print("not prime")