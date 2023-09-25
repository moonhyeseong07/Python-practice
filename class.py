def f(n):
    if n==1:
        print(n)
        return
    print(n)
    f(n-1)
n=map(int,input().split())
f(n)