def f(n,c=1):
    if c>n:
        return
    print("*"*c)
    f(n,c+1)
n=int(input())
f(n)
