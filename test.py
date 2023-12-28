limit=input()
m=limit[1]+limit[0]
m=int(m)*2
if(m>99):
    m=m%100
if(m<=50):
    print(m)
    print('GOOD')
else:
    print(m)
    print('OH MY GOD')
