b,g=input().split()
g=int(g)
y=int(b[:2])
if g==1 or g==2:
    y+=1900
else:
    y+=2000
age=2012-y+1
print(age)