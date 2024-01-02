n,ad,c=map(int,input().split())
if(ad-c==n):
    print("does not matter")
elif(ad-c>n):
    print('advertise')
else:
    print('do not advertise')