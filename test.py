def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y, x % y)
def gcdthree(a, b, c):
    return gcd(gcd(a,b),c)
a,b,c=map(int, input().split())
result = gcdthree(a, b, c)
print(result)