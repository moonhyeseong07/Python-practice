t,s=map(int,input().split())
lt=90-t
g=0
if lt%5==0:
    g=lt//5
else:
    g=lt//5+1
print(s+g)