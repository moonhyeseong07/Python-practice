def darius(k,d,a):
    if k+a<d or d==0:
        return "hasu"
    else:
        return "gosu"
k,d,a=map(int,input().split('/'))
print(darius(k,d,a))
