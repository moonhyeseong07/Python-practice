def f(n):
    if n>1:
        return n+f(n-1)
    else:
        return 1

if __name__=="__main__":
    n=int(input())
    a=f(n)
    for i in range(n):
        for j in range(i+1):
            print(a, end=' ')
            a-=1
        print('')