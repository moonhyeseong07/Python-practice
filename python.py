p=[]; q=[]
for i in range(3):
    a=int(input())
    p.append(a)
for i in range(2):
    a=int(input())
    q.append(a)
p=sorted(p); q=sorted(q)
f=p[0]+q[0]
print(f+f/10)