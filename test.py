a,b=map(int,input().split())
c=bool(int(a))
d=bool(int(b))
print((c and (not d)) == ((not c) and d))