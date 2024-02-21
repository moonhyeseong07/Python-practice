n=int(input())
for i in range(1,n+1,2):
    s=(n-i)//2
    star=i
    print(" "*s+"*"*star)