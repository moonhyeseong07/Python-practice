g,c,n=map=input().split()
n=int(n)
c=int(c)
if n<10:
    n='00'+str(n)
elif n<100:
    n='0'+str(n)
if c<10:
    c='0'+str(c)
print(g+str(c)+str(n))