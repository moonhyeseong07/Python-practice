def trans(n):
    if n//2==0:
        return str(n%2)
    return trans(n//2)+str(n%2)
n=int(input())
print(trans(n))
