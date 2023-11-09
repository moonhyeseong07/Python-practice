a,b=map(int,input().split())
def odd(a,b):
    if a>b:
        return 0
    elif b%2:
        odd(a,b-1)
        print(b,end=' ')
    else:
        odd(a,b-1)
odd(a,b)
