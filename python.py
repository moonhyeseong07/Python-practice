n=int(input())
a=list(map(int, input().split()))
b=sorted(a, reverse=True)
d={}
for i in range(n):
    if b[i] not in d:
        d[b[i]]=i+1
for i in range(n):
    print(a[i], d[a[i]])